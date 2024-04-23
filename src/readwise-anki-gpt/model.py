"""Module for Qt Models."""

from aqt import QAbstractItemModel, QTreeView, QApplication, QMainWindow, QModelIndex
from typing import Optional, List, Tuple, Any
from . import config
import sqlite3


class TreeItem:
    """
    Represents a single item (node) in a tree structure for the model.

    Attributes:
        parent_item (Optional[TreeItem]): The parent of this item.
        item_data (Tuple[Any, ...]): Data held by this item.
        child_items (List[TreeItem]): Children of this item.
    """

    def __init__(
        self, data: Tuple[Any, ...], parent: Optional["TreeItem"] = None
    ) -> None:
        """
        Initializes the TreeItem with data and parent.

        Args:
            data (Tuple[Any, ...]): The data to be stored in the item.
            parent (Optional[TreeItem]): The parent item. Defaults to None.
        """
        self.parent_item: Optional[TreeItem] = parent
        self.item_data: Tuple[Any, ...] = data
        self.child_items: List[TreeItem] = []

    def append_child(self, item: "TreeItem") -> None:
        """Appends a child item to this item."""
        self.child_items.append(item)

    def child(self, row: int) -> Optional["TreeItem"]:
        """Returns the child item at the specified row."""
        if row < 0 or row >= len(self.child_items):
            return None
        return self.child_items[row]

    def child_count(self) -> int:
        """Returns the number of children."""
        return len(self.child_items)

    def column_count(self) -> int:
        """Returns the number of columns of data."""
        return len(self.item_data)

    def data(self, column: int) -> Optional[Any]:
        """Returns the data at the specified column."""
        if column < 0 or column >= len(self.item_data):
            return None
        return self.item_data[column]

    def parent(self) -> Optional["TreeItem"]:
        """Returns the parent item."""
        return self.parent_item

    def row(self) -> int:
        """Returns the row of this item under its parent."""
        if self.parent_item:
            return self.parent_item.child_items.index(self)
        return 0


class TreeModel(QAbstractItemModel):
    """
    A model that interfaces between the SQLite database and a QTreeView.

    This model uses a tree structure to represent hierarchical data from the database.
    """

    def __init__(self, parent: Optional[QMainWindow] = None) -> None:
        """
        Initializes the tree model with a root item.
        """
        super().__init__(parent)
        self.root_item: TreeItem = TreeItem(("Title", "Author", "Highlight", "Card"))
        self.setup_model_data()

    def column_count(self, parent: QModelIndex = QModelIndex()) -> int:
        """Returns the number of columns for the children of the given parent."""
        return self.root_item.column_count()

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole) -> Optional[Any]:
        """Returns the data stored under the given role for the item referred to by the index."""
        if not index.isValid() or role != Qt.DisplayRole:
            return None
        item: TreeItem = index.internalPointer()
        return item.data(index.column())

    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        """Returns the item flags for the given index."""
        if not index.isValid():
            return Qt.NoItemFlags
        return super().flags(index)

    def header_data(
        self, section: int, orientation: Qt.Orientation, role: int = Qt.DisplayRole
    ) -> Optional[str]:
        """Returns the data for the given role and section in the header with the specified orientation."""
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.root_item.data(section)
        return None

    def index(
        self, row: int, column: int, parent: QModelIndex = QModelIndex()
    ) -> QModelIndex:
        """Creates an index in the model for a given row and column under the parent."""
        if not self.has_index(row, column, parent):
            return QModelIndex()

        parent_item: TreeItem = (
            self.root_item if not parent.isValid() else parent.internalPointer()
        )
        child_item: Optional[TreeItem] = parent_item.child(row)
        if child_item:
            return self.createIndex(row, column, child_item)
        return QModelIndex()

    def parent(self, index: QModelIndex) -> QModelIndex:
        """Finds the parent of the model item with the given index."""
        if not index.isValid():
            return QModelIndex()

        child_item: TreeItem = index.internalPointer()
        parent_item: Optional[TreeItem] = child_item.parent()

        if parent_item == self.root_item or not parent_item:
            return QModelIndex()

        return self.createIndex(parent_item.row(), 0, parent_item)

    def row_count(self, parent: QModelIndex = QModelIndex()) -> int:
        """Returns the number of rows under the given parent."""
        if parent.isValid() and parent.column() > 0:
            return 0

        parent_item: TreeItem = (
            self.root_item if not parent.isValid() else parent.internalPointer()
        )
        return parent_item.child_count()

    def setup_model_data(self) -> None:
        """Sets up the model data from the database."""
        with sqlite3.connect(config.READWISE_SQLITE_DATABASE_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT user_book_id, title, author FROM Book")
            books = cursor.fetchall()

            for book in books:
                book_item: TreeItem = TreeItem(book[1:3], self.root_item)
                self.root_item.append_child(book_item)

                cursor.execute("SELECT text FROM Highlight WHERE book_id=?", (book[0],))
                highlights = cursor.fetchall()

                for highlight in highlights:
                    highlight_item: TreeItem = TreeItem((highlight[0],), book_item)
                    book_item.append_child(highlight_item)

                    # Assuming Card is a transformation of Highlight here
                    card_item: TreeItem = TreeItem(
                        ("Card based on Highlight",), highlight_item
                    )
                    highlight_item.append_child(card_item)


class MainWindow(QMainWindow):
    """
    Main window for the application, hosting the tree view.
    """

    def __init__(self) -> None:
        """
        Initializes the main window with a tree view and sets the model.
        """
        super().__init__()
        self.tree_view: QTreeView = QTreeView(self)
        self.model: TreeModel = TreeModel()
        self.tree_view.setModel(self.model)
        self.setCentralWidget(self.tree_view)


if __name__ == "__main__":
    app: QApplication = QApplication([])
    main_window: MainWindow = MainWindow()
    main_window.show()
    app.exec()
