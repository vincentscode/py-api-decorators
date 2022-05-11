from py_api_decorators.json import JsonProperty, JsonObject
from py_api_decorators.api import BaseApiObject


class TestApiClass(JsonObject):
	@JsonProperty(mapping="test.str1.test")
	def str1() -> str: pass

	@JsonProperty(mapping="test.str1.test")
	def str2() -> int: pass

	@JsonProperty(mapping="test.str3.test", default=0)
	def str3() -> int: pass

	@JsonProperty(mapping="test.str3.test")
	def str4() -> int: pass

	@JsonProperty(mapping="test.str1.test")
	def str5(): pass

	def __init__(self, json_data):
		super().__init__(json_data)

t = TestApiClass.from_string('{ "test": { "str1": { "test": 1 } } }')
print("str1", type(t.str1), t.str1)
print("str2", type(t.str2), t.str2)
print("str3", type(t.str3), t.str3)
print("str5", type(t.str5), t.str5)