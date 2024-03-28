import pyautogui as py
import yfinance as yf
import pyperclip

bot_pause = 2
py.PAUSE = bot_pause

ticker = "BBAS3.SA"
nome = "Clisamax"
email_destino = "clisamax.gomes.dev@gmail.com"


def fetch_stock_data(ticker, period="6mo"):
    stock = yf.Ticker(ticker)
    data = stock.history(period)
    return data["Close"]


def buscar_maxima(fechamento):
    return fechamento.max()


def buscar_minima(fechamento):
    return fechamento.min()


def buscar_atual(fechamento):
    return fechamento.iloc[-1]


def conteúdo_email(ticker, max_price, min_price, atual_price):
    mensagem = f"""
        Bom dia,

        Segue abaixo as análises da ação {ticker} dos últimos seis meses:

        Cotação máxima: R$ {max_price}

        Cotação mínima: R$ {min_price}

        Cotação atual: R$ {atual_price}
    
        Atenciosamente, 
        {nome}
    """
    return mensagem


def abrir_email(nav):
    py.press("win")
    py.write(nav)
    py.press("enter")
    py.write("gmail.com")
    py.press("enter")


def escrever_email(mensagem_email):
    py.click(58, 170)
    py.write(email_destino)
    py.press("enter")
    py.press("tab")
    py.write(f" Ticker {ticker}")
    py.press("tab")
    pyperclip.copy(mensagem_email)
    py.hotkey(["ctrl", "v"])
    py.click(1899, 998)


def main(ticker):
    fechamento = fetch_stock_data(ticker)
    fechamento = round(fechamento, 2)
    max_price = buscar_maxima(fechamento)
    min_price = buscar_minima(fechamento)
    atual_price = buscar_atual(fechamento)
    mensagem_email = conteúdo_email(ticker, max_price, min_price, atual_price)
    abrir_email("edge")
    escrever_email(mensagem_email)


if __name__ == "__main__":
    main(ticker)
