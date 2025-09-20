from locust import HttpUser, task, between
import random

class EvaluacionesUser(HttpUser):
  wait_time = between(1, 3) # Cada usuario del test de carga espera entre 1 y 3 seg.

  @task
  def evaluarCrudClientes(self):
    # Mandar petición post a cliente para crear uno
    response = self.client.post("/clientes")
    if response.status_code == 200:
      # Del cliente creado obtener su ID
      id_cliente = response.json().get("id")

      # Obtener datos del cliente
      self.client.get("/clientes", params={
        "id": id_cliente
      })

      # Eliminar cliente
      self.client.delete("/clientes", params={
        "id": id_cliente
      })



