
class Division:
    @staticmethod
    def division(a,b):
        if isinstance(a,str) or isinstance(b,str):
            raise ValueError("Both inputs must be numbers.")
        return a/b

