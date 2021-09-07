print("Did we import successfully?")

try:
    import intro
    print("success")
    # import files are all runned at start
    # see how the code under main doesn't run from here
except Exception:
    print("fail")
