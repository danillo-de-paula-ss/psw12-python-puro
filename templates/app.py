from __init__ import input_datetime, input_float
from views.view import SubscriptionService, input_ask
from models.database import engine
from models.model import Subscription
from datetime import datetime
from decimal import Decimal

class UI:
    def __init__(self):
        self.subscription_service = SubscriptionService(engine)

    def start(self):
        while True:
            print("\n" + \
                "[1] -> Adicionar assinatura\n" + \
                "[2] -> Remover assinatura\n" + \
                "[3] -> Valor total\n" + \
                "[4] -> Gastos últimos 12 meses\n" + \
                "[5] -> Fazer o pagamento\n" + \
                "[6] -> Sair\n"
            )

            choice = int(input_ask("Escolha uma opção: ", valid_answers='123456'))

            # TODO: chamar o método pay na interface
            match choice:
                case 1:
                    self.add_subscription()
                case 2:
                    self.delete_subscription()
                case 3:
                    self.total_value()
                case 4:
                    self.subscription_service.gen_chart()
                case 5:
                    self.pay()
                case 6:
                    break

    def add_subscription(self):
        empresa = input('Empresa: ')
        site = input('Site: ')
        data_assinatura = input_datetime('Data de assinatura: ', format_='%d/%m/%Y')
        valor = Decimal(input_float('Valor: '))
        subscription = Subscription(empresa=empresa, site=site, data_assinatura=data_assinatura, valor=valor)
        self.subscription_service.create(subscription)
    
    def delete_subscription(self):
        subscriptions = self.subscription_service.list_all()
        # TODO: Quando excluir a assinatura, excluir todos os pagamentos dela
        print('Escolha qual assinatura deseja excluir')

        valid_answers = []
        for i in subscriptions:
            print(f'[{i.id}] -> {i.empresa}')
            valid_answers.append(str(i.id))
        
        choice = int(input_ask('Escolha a assinatura: ', valid_answers=valid_answers))
        self.subscription_service.delete(choice)
        print('Assinatura excluída com sucesso')

    def total_value(self):
        print(f'Seu valor total mensal em assinatura é: {self.subscription_service.total_value()}')

    def pay(self):
        subscriptions = self.subscription_service.list_all()
        print('Escolha qual assinatura deseja pagar esse mês')

        valid_answers = []
        for i, s in enumerate(subscriptions):
            print(f'[{i}] -> {s.empresa}')
            valid_answers.append(str(i))
        
        choice = int(input_ask('Escolha a assinatura: ', valid_answers=valid_answers))
        self.subscription_service.pay(subscriptions[choice])

if __name__ == '__main__':
    UI().start()
