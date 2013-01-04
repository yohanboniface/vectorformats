# -*- coding: utf-8 -*-

from lxml import etree
from xml.parsers.expat import ParserCreate


def schema(data, schema_path):
    """
    Validate an XML against a XSD.
    Raise an Exception if doesn't validate.
    """
    f = open(schema_path)
    schema_doc = etree.parse(f)
    xsd = etree.XMLSchema(schema_doc)
    xml = etree.XML(data)
    # assertValid will raise an exception if xml is not valid
    xsd.assertValid(xml)
    return True


def dtd(data, dtd_path):
    """
    Validate an XML against a DTD.
    Raise an Exception if doesn't validate.
    """
    dtd = etree.DTD(open(dtd_path, 'rb'))
    xml = etree.XML(data)
    return dtd.validate(xml)


def wellformed(data, encoding="utf-8"):
    """
    This check only the well-formedness.
    It's not a DTD based validation.
    Raise an Exception if doesn't validate.
    """
    parser = ParserCreate(encoding)
    # parser will raise an Exception if the output is not wellformed
    parser.Parse(data)
    return True
