import rpyc
from constRPYC import *
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  def exposed_value(self):
    print(f"Client requested the list. Current value: {self.value}")
    return self.value

  def exposed_append(self, data):
    self.value.append(data)
    print(f"Appended '{data}'. New list: {self.value}")
    return self.value


  def exposed_get_by_index(self, index):
    try:
      return self.value[index]
    except IndexError:
      return None 

  def exposed_search(self, data):
    return data in self.value

  def exposed_remove(self, data):
    try:
      self.value.remove(data)
      print(f"Removed '{data}'. New list: {self.value}")
      return True 
    except ValueError:
      return False 


  def exposed_insert(self, index, data):
    self.value.insert(index, data)
    print(f"Inserted '{data}' at index {index}. New list: {self.value}")
    return self.value
  

  def exposed_sort(self):
    self.value.sort()
    print(f"List sorted. New list: {self.value}")
    return self.value


  def exposed_clear(self):
    self.value = []
    print("List cleared.")
    return self.value

if __name__ == "__main__":
  print(f"Starting server on {SERVER}:{PORT}...")
  server = ThreadedServer(DBList(), port = PORT)
  server.start()