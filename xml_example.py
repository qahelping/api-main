from pydantic import BaseModel, Field, field_validator, AliasChoices
import xmltodict
class Book(BaseModel):
    name: str

xml_dict = """
<book> 
    <name>12345</name>
</book>   
"""

xml_dict = xmltodict.parse(xml_dict)['book']
print(xml_dict)
model = Book(**xml_dict)
print(model)

xml = xmltodict.unparse({'book': model.model_dump()})
print(xml)


