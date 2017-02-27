#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.9.0.11466 on 2017-02-27.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import practitioner
from .fhirdate import FHIRDate


class PractitionerTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Practitioner", js["resourceType"])
        return practitioner.Practitioner(js)
    
    def testPractitioner1(self):
        inst = self.instantiate_from("practitioner-example-f001-evdb.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner1(inst)
        
        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner1(inst2)
    
    def implPractitioner1(self, inst):
        self.assertEqual(inst.address[0].city, "Den Burg")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Galapagosweg 91")
        self.assertEqual(inst.address[0].postalCode, "9105 PZ")
        self.assertEqual(inst.address[0].use, "work")
        self.assertEqual(inst.birthDate.date, FHIRDate("1975-12-07").date)
        self.assertEqual(inst.birthDate.as_json(), "1975-12-07")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "f001")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.528.1.1007.3.1")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "938273695")
        self.assertEqual(inst.identifier[1].system, "urn:oid:2.16.840.1.113883.2.4.6.3")
        self.assertEqual(inst.identifier[1].use, "usual")
        self.assertEqual(inst.identifier[1].value, "129IDH4OP733")
        self.assertEqual(inst.name[0].family, "van den broek")
        self.assertEqual(inst.name[0].given[0], "Eric")
        self.assertEqual(inst.name[0].suffix[0], "MD")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "0205568263")
        self.assertEqual(inst.telecom[1].system, "email")
        self.assertEqual(inst.telecom[1].use, "work")
        self.assertEqual(inst.telecom[1].value, "E.M.vandenbroek@bmc.nl")
        self.assertEqual(inst.telecom[2].system, "fax")
        self.assertEqual(inst.telecom[2].use, "work")
        self.assertEqual(inst.telecom[2].value, "0205664440")
        self.assertEqual(inst.text.status, "generated")
    
    def testPractitioner2(self):
        inst = self.instantiate_from("practitioner-example-f002-pv.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner2(inst)
        
        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner2(inst2)
    
    def implPractitioner2(self, inst):
        self.assertEqual(inst.address[0].city, "Den Burg")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Galapagosweg 91")
        self.assertEqual(inst.address[0].postalCode, "9105 PZ")
        self.assertEqual(inst.address[0].use, "work")
        self.assertEqual(inst.birthDate.date, FHIRDate("1979-04-29").date)
        self.assertEqual(inst.birthDate.as_json(), "1979-04-29")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "f002")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.528.1.1007.3.1")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "730291637")
        self.assertEqual(inst.identifier[1].system, "urn:oid:2.16.840.1.113883.2.4.6.3")
        self.assertEqual(inst.identifier[1].use, "usual")
        self.assertEqual(inst.identifier[1].value, "174BIP3JH438")
        self.assertEqual(inst.name[0].family, "Voigt")
        self.assertEqual(inst.name[0].given[0], "Pieter")
        self.assertEqual(inst.name[0].suffix[0], "MD")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "0205569336")
        self.assertEqual(inst.telecom[1].system, "email")
        self.assertEqual(inst.telecom[1].use, "work")
        self.assertEqual(inst.telecom[1].value, "p.voigt@bmc.nl")
        self.assertEqual(inst.telecom[2].system, "fax")
        self.assertEqual(inst.telecom[2].use, "work")
        self.assertEqual(inst.telecom[2].value, "0205669382")
        self.assertEqual(inst.text.status, "generated")
    
    def testPractitioner3(self):
        inst = self.instantiate_from("practitioner-example-f003-mv.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner3(inst)
        
        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner3(inst2)
    
    def implPractitioner3(self, inst):
        self.assertEqual(inst.address[0].city, "Amsterdam")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Galapagosweg 91")
        self.assertEqual(inst.address[0].postalCode, "1105 AZ")
        self.assertEqual(inst.address[0].use, "work")
        self.assertEqual(inst.birthDate.date, FHIRDate("1963-07-01").date)
        self.assertEqual(inst.birthDate.as_json(), "1963-07-01")
        self.assertEqual(inst.communication[0].coding[0].code, "nl")
        self.assertEqual(inst.communication[0].coding[0].display, "Dutch")
        self.assertEqual(inst.communication[0].coding[0].system, "urn:oid:2.16.840.1.113883.6.121")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "f003")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.528.1.1007.3.1")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "846100293")
        self.assertEqual(inst.identifier[1].system, "urn:oid:2.16.840.1.113883.2.4.6.3")
        self.assertEqual(inst.identifier[1].use, "usual")
        self.assertEqual(inst.identifier[1].value, "243HID3RT938")
        self.assertEqual(inst.name[0].family, "Versteegh")
        self.assertEqual(inst.name[0].given[0], "Marc")
        self.assertEqual(inst.name[0].suffix[0], "MD")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "0205562431")
        self.assertEqual(inst.telecom[1].system, "email")
        self.assertEqual(inst.telecom[1].use, "work")
        self.assertEqual(inst.telecom[1].value, "m.versteegh@bmc.nl")
        self.assertEqual(inst.telecom[2].system, "fax")
        self.assertEqual(inst.telecom[2].use, "work")
        self.assertEqual(inst.telecom[2].value, "0205662948")
        self.assertEqual(inst.text.status, "generated")
    
    def testPractitioner4(self):
        inst = self.instantiate_from("practitioner-example-f004-rb.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner4(inst)
        
        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner4(inst2)
    
    def implPractitioner4(self, inst):
        self.assertEqual(inst.address[0].city, "Amsterdam")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Galapagosweg 91")
        self.assertEqual(inst.address[0].postalCode, "1105 AZ")
        self.assertEqual(inst.address[0].use, "work")
        self.assertEqual(inst.birthDate.date, FHIRDate("1980-02-04").date)
        self.assertEqual(inst.birthDate.as_json(), "1980-02-04")
        self.assertEqual(inst.communication[0].coding[0].code, "nl")
        self.assertEqual(inst.communication[0].coding[0].display, "Netherlands")
        self.assertEqual(inst.communication[0].coding[0].system, "urn:oid:2.16.840.1.113883.6.121")
        self.assertEqual(inst.communication[0].text, "Language")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "f004")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.528.1.1007.3.1")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "118265112")
        self.assertEqual(inst.identifier[1].system, "urn:oid:2.16.840.1.113883.2.4.6.3")
        self.assertEqual(inst.identifier[1].use, "usual")
        self.assertEqual(inst.identifier[1].value, "523ASA1LK927")
        self.assertEqual(inst.name[0].family, "Briet")
        self.assertEqual(inst.name[0].given[0], "Ronald")
        self.assertEqual(inst.name[0].suffix[0], "MD")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "0205569273")
        self.assertEqual(inst.telecom[1].system, "email")
        self.assertEqual(inst.telecom[1].use, "work")
        self.assertEqual(inst.telecom[1].value, "r.briet@bmc.nl")
        self.assertEqual(inst.telecom[2].system, "fax")
        self.assertEqual(inst.telecom[2].use, "work")
        self.assertEqual(inst.telecom[2].value, "0205664440")
        self.assertEqual(inst.text.status, "generated")
    
    def testPractitioner5(self):
        inst = self.instantiate_from("practitioner-example-f005-al.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner5(inst)
        
        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner5(inst2)
    
    def implPractitioner5(self, inst):
        self.assertEqual(inst.address[0].city, "Amsterdam")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Galapagosweg 9")
        self.assertEqual(inst.address[0].postalCode, "1105 AZ")
        self.assertEqual(inst.address[0].use, "work")
        self.assertEqual(inst.birthDate.date, FHIRDate("1959-03-11").date)
        self.assertEqual(inst.birthDate.as_json(), "1959-03-11")
        self.assertEqual(inst.communication[0].coding[0].code, "fr")
        self.assertEqual(inst.communication[0].coding[0].display, "France")
        self.assertEqual(inst.communication[0].coding[0].system, "urn:oid:2.16.840.1.113883.6.121")
        self.assertEqual(inst.gender, "female")
        self.assertEqual(inst.id, "f005")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.528.1.1007.3.1")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "118265112")
        self.assertEqual(inst.identifier[1].system, "urn:oid:2.16.840.1.113883.2.4.6.3")
        self.assertEqual(inst.identifier[1].use, "usual")
        self.assertEqual(inst.identifier[1].value, "191REW8WE916")
        self.assertEqual(inst.name[0].family, "Anne")
        self.assertEqual(inst.name[0].given[0], "Langeveld")
        self.assertEqual(inst.name[0].suffix[0], "MD")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.photo[0].contentType, "image/jpeg")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "0205563847")
        self.assertEqual(inst.telecom[1].system, "email")
        self.assertEqual(inst.telecom[1].use, "work")
        self.assertEqual(inst.telecom[1].value, "a.langeveld@bmc.nl")
        self.assertEqual(inst.telecom[2].system, "fax")
        self.assertEqual(inst.telecom[2].use, "work")
        self.assertEqual(inst.telecom[2].value, "0205668916")
        self.assertEqual(inst.text.status, "generated")
    
    def testPractitioner6(self):
        inst = self.instantiate_from("practitioner-example-f006-rvdb.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner6(inst)
        
        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner6(inst2)
    
    def implPractitioner6(self, inst):
        self.assertEqual(inst.address[0].city, "Den Burg")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Galapagosweg 91")
        self.assertEqual(inst.address[0].postalCode, "9105 PZ")
        self.assertEqual(inst.address[0].use, "work")
        self.assertEqual(inst.birthDate.date, FHIRDate("1975-12-07").date)
        self.assertEqual(inst.birthDate.as_json(), "1975-12-07")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "f006")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.528.1.1007.3.1")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "937223645")
        self.assertEqual(inst.identifier[1].system, "urn:oid:2.16.840.1.113883.2.4.6.3")
        self.assertEqual(inst.identifier[1].use, "usual")
        self.assertEqual(inst.identifier[1].value, "134IDY41W988")
        self.assertEqual(inst.name[0].family, "van den Berk")
        self.assertEqual(inst.name[0].given[0], "Rob")
        self.assertEqual(inst.name[0].suffix[0], "MD")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "0205569288")
        self.assertEqual(inst.telecom[1].system, "email")
        self.assertEqual(inst.telecom[1].use, "work")
        self.assertEqual(inst.telecom[1].value, "R.A.vandenberk@bmc.nl")
        self.assertEqual(inst.telecom[2].system, "fax")
        self.assertEqual(inst.telecom[2].use, "work")
        self.assertEqual(inst.telecom[2].value, "0205664987")
        self.assertEqual(inst.text.status, "generated")
    
    def testPractitioner7(self):
        inst = self.instantiate_from("practitioner-example-f007-sh.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner7(inst)
        
        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner7(inst2)
    
    def implPractitioner7(self, inst):
        self.assertEqual(inst.address[0].city, "Den Burg")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Galapagosweg 91")
        self.assertEqual(inst.address[0].postalCode, "9105 PZ")
        self.assertEqual(inst.address[0].use, "work")
        self.assertEqual(inst.birthDate.date, FHIRDate("1971-11-07").date)
        self.assertEqual(inst.birthDate.as_json(), "1971-11-07")
        self.assertEqual(inst.gender, "female")
        self.assertEqual(inst.id, "f007")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.528.1.1007.3.1")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "874635264")
        self.assertEqual(inst.identifier[1].system, "urn:oid:2.16.840.1.113883.2.4.6.3")
        self.assertEqual(inst.identifier[1].use, "usual")
        self.assertEqual(inst.identifier[1].value, "567IUI51C154")
        self.assertEqual(inst.name[0].family, "Heps")
        self.assertEqual(inst.name[0].given[0], "Simone")
        self.assertEqual(inst.name[0].suffix[0], "MD")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "020556936")
        self.assertEqual(inst.telecom[1].system, "email")
        self.assertEqual(inst.telecom[1].use, "work")
        self.assertEqual(inst.telecom[1].value, "S.M.Heps@bmc.nl")
        self.assertEqual(inst.telecom[2].system, "fax")
        self.assertEqual(inst.telecom[2].use, "work")
        self.assertEqual(inst.telecom[2].value, "0205669283")
        self.assertEqual(inst.text.status, "generated")
    
    def testPractitioner8(self):
        inst = self.instantiate_from("practitioner-example-f201-ab.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner8(inst)
        
        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner8(inst2)
    
    def implPractitioner8(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].city, "Den helder")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Walvisbaai 3")
        self.assertEqual(inst.address[0].line[1], "C4 - Automatisering")
        self.assertEqual(inst.address[0].postalCode, "2333ZA")
        self.assertEqual(inst.address[0].use, "work")
        self.assertEqual(inst.birthDate.date, FHIRDate("1956-12-24").date)
        self.assertEqual(inst.birthDate.as_json(), "1956-12-24")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.528.1.1007.3.1")
        self.assertEqual(inst.identifier[0].type.text, "UZI-nummer")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "12345678901")
        self.assertEqual(inst.name[0].family, "Bronsig")
        self.assertEqual(inst.name[0].given[0], "Arend")
        self.assertEqual(inst.name[0].prefix[0], "Dr.")
        self.assertEqual(inst.name[0].text, "Dokter Bronsig")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.qualification[0].code.coding[0].code, "41672002")
        self.assertEqual(inst.qualification[0].code.coding[0].display, "Pulmonologist")
        self.assertEqual(inst.qualification[0].code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "+31715269111")
        self.assertEqual(inst.text.status, "generated")
    
    def testPractitioner9(self):
        inst = self.instantiate_from("practitioner-example-f202-lm.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner9(inst)
        
        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner9(inst2)
    
    def implPractitioner9(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].city, "Den helder")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Walvisbaai 3")
        self.assertEqual(inst.address[0].line[1], "C4 - Automatisering")
        self.assertEqual(inst.address[0].postalCode, "2333ZA")
        self.assertEqual(inst.address[0].use, "work")
        self.assertEqual(inst.birthDate.date, FHIRDate("1960-06-12").date)
        self.assertEqual(inst.birthDate.as_json(), "1960-06-12")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "f202")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.528.1.1007.3.1")
        self.assertEqual(inst.identifier[0].type.text, "UZI-nummer")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "12345678902")
        self.assertEqual(inst.identifier[1].system, "https://www.bigregister.nl/")
        self.assertEqual(inst.identifier[1].type.text, "BIG-nummer")
        self.assertEqual(inst.identifier[1].use, "official")
        self.assertEqual(inst.identifier[1].value, "12345678902")
        self.assertEqual(inst.name[0].family, "Maas")
        self.assertEqual(inst.name[0].given[0], "Luigi")
        self.assertEqual(inst.name[0].prefix[0], "Dr.")
        self.assertEqual(inst.name[0].text, "Luigi Maas")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "+31715269111")
        self.assertEqual(inst.text.status, "generated")
    
    def testPractitioner10(self):
        inst = self.instantiate_from("practitioner-example-f203-jvg.json")
        self.assertIsNotNone(inst, "Must have instantiated a Practitioner instance")
        self.implPractitioner10(inst)
        
        js = inst.as_json()
        self.assertEqual("Practitioner", js["resourceType"])
        inst2 = practitioner.Practitioner(js)
        self.implPractitioner10(inst2)
    
    def implPractitioner10(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].city, "Den helder")
        self.assertEqual(inst.address[0].country, "NLD")
        self.assertEqual(inst.address[0].line[0], "Walvisbaai 3")
        self.assertEqual(inst.address[0].postalCode, "2333ZA")
        self.assertEqual(inst.address[0].use, "work")
        self.assertEqual(inst.birthDate.date, FHIRDate("1983-04-20").date)
        self.assertEqual(inst.birthDate.as_json(), "1983-04-20")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "f203")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.528.1.1007.3.1")
        self.assertEqual(inst.identifier[0].type.text, "UZI-nummer")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "12345678903")
        self.assertEqual(inst.identifier[1].system, "https://www.bigregister.nl/")
        self.assertEqual(inst.identifier[1].type.text, "BIG-nummer")
        self.assertEqual(inst.identifier[1].use, "official")
        self.assertEqual(inst.identifier[1].value, "12345678903")
        self.assertEqual(inst.name[0].text, "Juri van Gelder")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "+31715269111")
        self.assertEqual(inst.text.status, "generated")

