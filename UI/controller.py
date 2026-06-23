import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
        anni = self._model.getAnni()
        for anno in anni:
            self._view._ddYear1.options.append(ft.dropdown.Option(anno))
            self._view._ddYear2.options.append(ft.dropdown.Option(anno))



    def handleBuildGraph(self, e):
        y1 = min(int(self._view._ddYear1.value), int(self._view._ddYear2.value))
        y2 = max(int(self._view._ddYear1.value), int(self._view._ddYear2.value))
        n, a = self._model.creaGrafo(y1, y2)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {n} nodi e {a} archi"))
        self._view.update_page()

    def handlePrintDetails(self, e):
        self._model.stampaDettagli()

    def handleCercaDreamChampionship(self, e):
        pass


