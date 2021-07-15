class ErrorPatente(Exception):
    def __init__(self, conductor):
        super().__init__(f"Esta patenete {conductor.patente} no es la que tiene asociada "
                         f"{conductor.nombre} en el registro oficial")
        self.conductor = conductor


