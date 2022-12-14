from botcity.core import DesktopBot
import pyautogui as pag


class Bot(DesktopBot):
    def action(self, execution=None):
        """
        Execução principal
        """
        reservas = []
        observacao = pag.prompt("Observação")
        nova_data = pag.prompt("Data [dd/mm/aaaa]")
        qtd_reservas = int(pag.prompt("Quantidade de reservas"))

        for numero in range(0, qtd_reservas):
            reservas.append(int(pag.prompt(f"{numero + 1}º Reserva")))

        # Opens the TFP website.
        self.browse(
            "https://timformaplus.timbrasil.com.br/_vacbt/gac_prorrogar_reserva/listar.aspx?codigoMenu=217"
        )

        for reserva in reservas:
            if not self.find(
                "localiza_campo_protocolo", matching=0.97, waiting_time=10000
            ):
                self.not_found("localiza_campo_protocolo")
            self.double_click_relative(430, 6)

            self.paste(reserva, wait=5000)
            self.key_enter(wait=1000)

            if not self.find(
                "localiza_editar_reserva", matching=0.97, waiting_time=10000
            ):
                self.not_found("localiza_editar_reserva")
            self.click()

            if not self.find(
                "localiza_campo_data", matching=0.97, waiting_time=10000
            ):
                self.not_found("localiza_campo_data")
            self.click_relative(266, 12)

            self.paste(nova_data, wait=5000)
            self.tab(wait=100)
            self.paste(observacao, wait=5000)
            self.tab(wait=100)
            self.key_enter(wait=5000)

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == "__main__":
    Bot.main()
