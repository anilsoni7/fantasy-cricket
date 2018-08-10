import math

from PyQt5.QtCore import QAbstractTableModel, QByteArray, QDir, QStorageInfo, Qt
from PyQt5.QtWidgets import QAbstractItemView, QApplication, QTreeView


def sizeToString(size):
    if size <= 0:
        return "0 b"
    decimals = 2
    units = ["b", "kB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
    power = int(math.log(size, 1024))
    try:
        unit = units[power]
    except IndexError:
        unit = units[-1]
        power = len(units) - 1
    if power == 0:
        decimals = 0
    normsize = size / math.pow(1024, power)
    #: this should expand to "1.23 GB"
    return "%0.*f %s" % (decimals, normsize, unit)


class StorageModel(QAbstractTableModel):
    ColumnRootPath, ColumnName, ColumnDevice, ColumnFileSystemName, \
    ColumnTotal, ColumnFree, ColumnAvailable, ColumnIsReady, \
    ColumnIsReadOnly, ColumnIsValid, ColumnCount = range(11)

    columnFuncMap = {
        ColumnRootPath: lambda volume: QDir.toNativeSeparators(volume.rootPath()),
        ColumnName: lambda volume: volume.name(),
        ColumnDevice: lambda volume: volume.device(),
        ColumnFileSystemName: lambda volume: volume.fileSystemType(),
        ColumnTotal: lambda volume: sizeToString(volume.bytesTotal()),
        ColumnFree: lambda volume: sizeToString(volume.bytesFree()),
        ColumnAvailable: lambda volume: sizeToString(volume.bytesAvailable()),
        ColumnIsReady: lambda volume: volume.isReady(),
        ColumnIsReadOnly: lambda volume: volume.isReadOnly(),
        ColumnIsValid: lambda volume: volume.isValid(),
    }

    columnNameMap = {
        ColumnRootPath: "Root path",
        ColumnName: "Volume Name",
        ColumnDevice: "Device",
        ColumnFileSystemName: "File system",
        ColumnTotal: "Total",
        ColumnFree: "Free",
        ColumnAvailable: "Available",
        ColumnIsReady: "Ready",
        ColumnIsReadOnly: "Read-only",
        ColumnIsValid: "Valid",
    }

    def __init__(self, parent = None):
        super(StorageModel, self).__init__(parent)
        self.volumes = QStorageInfo.mountedVolumes()

    def columnCount(self, parent = None):
        return self.ColumnCount

    def rowCount(self, parent):
        if parent.isValid():
            return 0
        return len(self.volumes)

    def data(self, index, role):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            volume = self.volumes[index.row()]
            func = self.columnFuncMap.get(index.column())
            if func is not None:
                return func(volume)

        elif role == Qt.ToolTipRole:
            volume = self.volumes[index.row()]
            tooltip = []
            for column in range(self.ColumnCount):
                label = self.columnNameMap.get(column)
                value = self.columnFuncMap[column](volume)
                if isinstance(value, QByteArray):
                    value = str(bytes(value).decode('utf-8'))
                tooltip.append("{0}: {1}".format(label, value))
            return "\n".join(tooltip)

    def headerData(self, section, orientation, role):
        if orientation != Qt.Horizontal:
            return None
        if role != Qt.DisplayRole:
            return None
        return self.columnNameMap.get(section)


def main(args):
    app = QApplication (args)
    view = QTreeView()
    view.setModel(StorageModel(view))
    view.resize(640, 480)
    view.setSelectionBehavior(QAbstractItemView.SelectRows)
    for column in range(view.model().columnCount()):
        view.resizeColumnToContents(column)
    view.show()
    return app.exec_()


if __name__ == '__main__':
    import sys
    main(sys.argv)
