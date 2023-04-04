import ast
# print(ast.dump(ast.parse('True if b else False', mode='eval'), indent=4))

# print(ast.dump(ast.parse('True if x > y else False', mode='eval'), indent=4))

print(ast.dump(ast.parse('False if z > a > x else True', mode='eval'), indent=4))



# print(ast.dump(ast.parse('''
# y = y - 1'''''),
#  indent=4))

# print(ast.dump(ast.parse('''
# y = 5 
# y = y - 1'''''),
#  indent=4))

# print(ast.dump(ast.parse('''
# y = 5 
# y -= 1'''''),
#  indent=4))






# code = """class Alcancia:

#             def __init__(self, color, n_monedas):
#                 self.color = color
#                 self.n_monedas = n_monedas

#             def pagos_del_mes(self, n_monedas):
#                 self.n_monedas = self.monedas - 100 
# """
# print(ast.dump(ast.parse(code), indent=4))

# Module(
#     body=[
#         ClassDef(
#             name='Alcancia',
#             bases=[],
#             keywords=[],
#             body=[
#                 FunctionDef(
#                     name='__init__',
#                     args=arguments(
#                         posonlyargs=[],
#                         args=[
#                             arg(arg='self'),
#                             arg(arg='color'),
#                             arg(arg='n_monedas')],
#                         kwonlyargs=[],
#                         kw_defaults=[],
#                         defaults=[]),
#                     body=[
#                         Assign(
#                             targets=[
#                                 Attribute(
#                                     value=Name(id='self', ctx=Load()),
#                                     attr='color',
#                                     ctx=Store())],
#                             value=Name(id='color', ctx=Load())),
#                         Assign(
#                             targets=[
#                                 Attribute(
#                                     value=Name(id='self', ctx=Load()),
#                                     attr='n_monedas',
#                                     ctx=Store())],
#                             value=Name(id='n_monedas', ctx=Load()))],
#                     decorator_list=[]),
#                 FunctionDef(
#                     name='pagos_del_mes',
#                     args=arguments(
#                         posonlyargs=[],
#                         args=[
#                             arg(arg='self'),
#                             arg(arg='n_monedas')],
#                         kwonlyargs=[],
#                         kw_defaults=[],
#                         defaults=[]),
#                     body=[
#                         Assign(
#                             targets=[
#                                 Attribute(
#                                     value=Name(id='self', ctx=Load()),
#                                     attr='n_monedas',
#                                     ctx=Store())],
#                             value=BinOp(
#                                 left=Attribute(
#                                     value=Name(id='self', ctx=Load()),
#                                     attr='monedas',
#                                     ctx=Load()),
#                                 op=Sub(),
#                                 right=Constant(value=100)))],
#                     decorator_list=[])],
#             decorator_list=[])],
#     type_ignores=[])


# code = """class Alcancia:

#             def __init__(self, color, n_monedas):
#                 self.color = color
#                 self.n_monedas = n_monedas

#             def pagos_del_mes(self, n_monedas):
#                 self.n_monedas -= 100 
# """

# print(ast.dump(ast.parse(code), indent=4))

# Module(
#     body=[
#         ClassDef(
#             name='Alcancia',
#             bases=[],
#             keywords=[],
#             body=[
#                 FunctionDef(
#                     name='__init__',
#                     args=arguments(
#                         posonlyargs=[],
#                         args=[
#                             arg(arg='self'),
#                             arg(arg='color'),
#                             arg(arg='n_monedas')],
#                         kwonlyargs=[],
#                         kw_defaults=[],
#                         defaults=[]),
#                     body=[
#                         Assign(
#                             targets=[
#                                 Attribute(
#                                     value=Name(id='self', ctx=Load()),
#                                     attr='color',
#                                     ctx=Store())],
#                             value=Name(id='color', ctx=Load())),
#                         Assign(
#                             targets=[
#                                 Attribute(
#                                     value=Name(id='self', ctx=Load()),
#                                     attr='n_monedas',
#                                     ctx=Store())],
#                             value=Name(id='n_monedas', ctx=Load()))],
#                     decorator_list=[]),
#                 FunctionDef(
#                     name='pagos_del_mes',
#                     args=arguments(
#                         posonlyargs=[],
#                         args=[
#                             arg(arg='self'),
#                             arg(arg='n_monedas')],
#                         kwonlyargs=[],
#                         kw_defaults=[],
#                         defaults=[]),
#                     body=[
#                         AugAssign(
#                             target=Attribute(
#                                 value=Name(id='self', ctx=Load()),
#                                 attr='n_monedas',
#                                 ctx=Store()),
#                             op=Sub(),
#                             value=Constant(value=100))],
#                     decorator_list=[])],
#             decorator_list=[])],
#     type_ignores=[])