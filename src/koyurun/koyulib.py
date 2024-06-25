
def koyureverse(s: str) -> str:
    """こゆるんのリバース関数(1)

    Args:
        s (str): 反転させる文字列

    Returns:
        str: 反転した文字列
    """
    return s[::-1]

def koyuupper(s: str) -> str:
    """こゆるんのアッパーケース関数

    Args:
        s (str): 大文字に変換する文字列

    Returns:
        str: 大文字に変換した文字列
    """
    return s.upper()


def koyulower(s: str) -> str:
    """こゆるんのロウアーケース関数

    Args:
        s (str): 小文字に変換する文字列

    Returns:
        str: 小文字に変換した文字列
    """
    return s.lower()
