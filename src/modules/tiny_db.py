from dataclasses import asdict, dataclass
from typing import Literal

from tinydb import Query, TinyDB


@dataclass
class Todo:
	task: str
	owner: str
	status: Literal['done', 'todo'] = 'todo'

	def as_dict(self):
		return asdict(self)

	@classmethod
	def from_dict(cls, data):
		return Todo(**data)



t1 = Todo('Buy coffee', 'Luiz', 'todo')
t2 = Todo('Walk the dog', 'Luiz', 'todo')


db = TinyDB('./db.json', indent=4)
db.truncate()
index_1 = db.insert(t1.as_dict())
# db.insert_multiple([])
# db.remove(doc_ids=[1])
print('index:',index_1)
print(db.get(doc_id=index_1))
db.update(
	{'task':'Buy more coffee'},
	doc_ids=[index_1]
)
print(db.get(doc_id=index_1))


TodoQuery = Query()
print(	
	db.search(
		TodoQuery.task.search('coffee')
	)	
)