from langchain.tools import tool


class CalculatorTools:
    @tool("Make calculation")
    def calculate(operation):
        """
        Utile pour réaliser des calculs mathématiques,
        comme l'addition, la soustraction, la multiplication, la division,
        la comparaison entre deux chiffres, etc.
        L'argument passé à cet outil doit être une expression mathématique,
        voilà deux exemples '200*7 ou '5000/2*10' ou 'x >= y'
        """
        try:
            return eval(operation)
        except SyntaxError:
            return "Error : invalid syntax in math expression"
