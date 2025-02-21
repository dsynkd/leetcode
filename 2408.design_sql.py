class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.ids = dict()
        self.tables = dict()
        self.colCount = dict()
        for i in range(len(names)):
            self.ids[names[i]] = 1
            self.tables[names[i]] = dict()
            self.colCount[names[i]] = columns[i]

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.tables or self.colCount[name] != len(row):
            return False
        id = self.ids[name]
        self.tables[name][id] = row
        self.ids[name] += 1
        return True

    def rmv(self, name: str, rowId: int) -> None:
        if name not in self.tables:
            return
        table = self.tables[name]
        if rowId not in table:
            return
        del table[rowId]

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.tables:
            return "<null>"
        table = self.tables[name]
        if rowId not in table:
            return "<null>"
        row = table[rowId]
        if columnId > len(row):
            return "<null>"
        return row[columnId-1]

    def exp(self, name: str) -> List[str]:
        if name not in self.tables:
            return []
        table = self.tables[name]
        return [str(id) + ',' + ','.join(row) for id, row in table.items()]
