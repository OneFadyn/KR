from gigachat import GigaChat


class Copilot:

    def get_answer(self, question):
        # Используйте токен, полученный в личном кабинете из поля Авторизационные данные
        with GigaChat(
                credentials='YTQ3ZmUyZmUtZjYzYS00NTBlLWIyOTAtODZjMWRmMjkzZTkxOjdiNmJkY2IxLThkMzAtNDdkMi04ZmI1LWFkZGFiZjUwOGRhNQ==',
                verify_ssl_certs=False) as giga:
            response = giga.chat(question)
            print(f'-{question}')
            print(f'-{response.choices[0].message.content}')

        return response.choices[0].message.content
