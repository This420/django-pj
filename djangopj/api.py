from ninja_extra import NinjaExtraAPI, api_controller, http_get

api = NinjaExtraAPI()

@api.get("/add", tags=['Math'])
def add(request, a: int, b: int):
	return {"result:": a + b}

@api_controller('/', tags=['Math'], permissions=[])
class MathAPI:
	@http_get('/subtract',)
	def substract(self, a:int, b:int):
		return {"result": a - b}

api.register_controllers(
	MathAPI
)
