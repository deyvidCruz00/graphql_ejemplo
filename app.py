from flask import Flask
from flask_graphql import GraphQLView
import graphene

# ==== Datos quemados ====
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 3500.0, "stock": 10},
    {"id": 2, "nombre": "Mouse", "precio": 80.5, "stock": 50},
    {"id": 3, "nombre": "Teclado", "precio": 120.0, "stock": 30},
]


# ==== Definición del tipo Producto ====
class Producto(graphene.ObjectType):
    id = graphene.Int()
    nombre = graphene.String()
    precio = graphene.Float()
    stock = graphene.Int()


# ==== Definición de las consultas ====
class Query(graphene.ObjectType):
    # Obtener todos los productos
    productos = graphene.List(Producto)

    # Obtener un producto por ID
    producto = graphene.Field(Producto, id=graphene.Int(required=True))

    def resolve_productos(self, info):
        return productos

    def resolve_producto(self, info, id):
        for p in productos:
            if p["id"] == id:
                return p
        return None


# ==== Definición de las mutaciones ====
class CrearProducto(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        precio = graphene.Float(required=True)
        stock = graphene.Int(required=True)

    producto = graphene.Field(Producto)

    def mutate(self, info, nombre, precio, stock):
        nuevo = {
            "id": len(productos) + 1,
            "nombre": nombre,
            "precio": precio,
            "stock": stock,
        }
        productos.append(nuevo)
        return CrearProducto(producto=nuevo)


class Mutation(graphene.ObjectType):
    crear_producto = CrearProducto.Field()


# ==== Crear el esquema ====
schema = graphene.Schema(query=Query, mutation=Mutation)


# ==== Servidor Flask con GraphQL ====
app = Flask(__name__)

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True),  # UI de prueba
)

if __name__ == "__main__":
    app.run(debug=True)
