cls_held=int(input("hom many days cls held"))
cls_att=int(input("how many days attend"))

total=(cls_att/cls_held)*100
if total>75:
    print("allow to exam")
else:
    print("not allow exam")
