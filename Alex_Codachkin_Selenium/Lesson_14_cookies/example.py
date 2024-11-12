def reserve_table(key, value):
    if tables.get(key) is None:
        tables[key] = value
    else:
        pass


def delete_reservation(x):
    if tables.get(x) is not None:
        tables[x] = None


tables = {
  1: 'Andrey',
  2: None,
  3: None,
  4: None,
  5: None,
  6: None,
  7: None,
  8: None,
  9: None,
}
reserve_table(1, 'Artur')
print(tables)
