class SequenceElement:
    def __init__(self):
        self.name = ''
        self.type = ''

    def create_node(self, element):
        pass

class FragmentReference(SequenceElement):
    def __init__(self):
        self.type = 'Fragment'

    def create_node(self, element):
        self.name = element["name"]

class Message(SequenceElement):
    def __init__(self):
        super().__init__()
        self.type = 'Message'
        self.message_type = ''
        self.prob = ''
        self.source = ''
        self.target = ''

    def create_node(self, element):
        try:
            self.name = element["name"]
            if element["message_type"] != 'sync' and element["message_type"] != 'async' and element["message_type"] != 'reply':
                raise Exception("InvalidMessageTypeException")
            self.message_type = element["message_type"]
            self.prob = element["prob"]
            self.source = element["source"]
            self.target = element["target"]
        except:
            raise Exception("MessageFormatException")

class Fragment:
    def __init__(self, name, representedBy):
        self.name = name
        self.representedBy = representedBy


class Lifeline:
    def __init__(self, name):
        self.name = name


class SequenceDiagram:
    def __init__(self, name, guard_condition, elements):
        self.name = name
        self.guard_condition = guard_condition
        self.elements = elements


def extracted_sequence_diagram():
    global SequenceDiagrams

    class SequenceDiagrams():
        def __init__(self, diagram):
            self.lifelines = []
            self.fragments = []
            self.diagrams = []

            for element in diagram["Lifelines"]:
                lifeline = Lifeline(element["name"])
                self.lifelines.append(lifeline)

            for element in diagram["Fragments"]:
                try:
                    fragment = Fragment(element["name"], element["representedBy"])
                    self.fragments.append(fragment)
                except:
                    raise Exception("EmptyOptionalFragment")

            for sequence_diagram in diagram["SequenceDiagrams"]:
                try:
                    elements = []
                    my_types = {
                        "Fragment": FragmentReference(),
                        "Message": Message()
                    }

                    for element in sequence_diagram["elements"]:
                        node = my_types[element["type"]]
                        node.create_node(element)
                        elements.append(node)

                    this_diagram = SequenceDiagram(sequence_diagram["name"],
                                                   sequence_diagram["guard_condition"],
                                                   elements)
                    self.diagrams.append(this_diagram)
                except:
                    raise Exception("EmptyGuardConditionException")

        def getDiagrams(self):
            return self.diagrams

        def getXml(self, file):

            print('<SequenceDiagrams>', file=file)
            print('\t<Lifelines>', file=file)
            for lifeline in self.lifelines:
                print('\t\t<Lifeline name="{}" />'.format(lifeline.name), file=file)
            print('\t</Lifelines>', file=file)

            print('\t<Fragments>', file=file)
            for fragment in self.fragments:
                print('\t\t<Optional name="{}" representedBy="{}" />'.format(fragment.name, fragment.representedBy),
                      file=file)
            print('\t</Fragments>', file=file)
            for diagram in self.diagrams:
                print('\t<SequenceDiagram name="{}" guardCondition="{}">'.format(diagram.name, diagram.guard_condition),
                      file=file)
                for element in diagram.elements:
                    if element.type == 'Message':
                        print('\t\t<Message type="{}" name="{}" prob="{}" source="{}" target="{}" />'.format(
                            element.message_type, element.name, element.prob, element.source, element.target),
                              file=file)
                    else:
                        print('\t\t<Fragment name="{}" />'.format(element.name), file=file)

                print('\t</SequenceDiagram>', file=file)
            print('<SequenceDiagrams>', file=file)


extracted_sequence_diagram()


