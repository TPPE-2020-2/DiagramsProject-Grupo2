class SequenceElement:
    def __init__(self, name):
        self.name=name
        self.type=''

class FragmentReference(SequenceElement):
    def __init__(self, name):
        super().__init__(name)
        self.type='Fragment'

class Message(SequenceElement):
    def __init__(self, name, message_type, prob, source, target):
        super().__init__(name)
        self.type='Message'
        if message_type != 'sync' and message_type != 'async' and message_type != 'reply':
            raise Exception("InvalideMessageTypeException")
        self.message_type=message_type
        self.prob=prob
        self.source=source
        self.target=target
            

class Fragment:
    def __init__(self, name, representedBy):
        self.name=name
        self.representedBy=representedBy

class Lifeline:
    def __init__(self, name):
        self.name=name

class SequenceDiagram:
    def __init__(self, name, guard_condition, elements):
        self.name=name
        self.guard_condition=guard_condition
        self.elements=elements

class SequenceDiagrams():
    def __init__(self, diagram):
        self.lifelines=[]
        self.fragments=[]
        self.diagrams=[]

        for element in diagram["Lifelines"]:
            lifeline=Lifeline(element["name"])
            self.lifelines.append(lifeline)

        for element in diagram["Fagments"]:
            try:
                fragment=Fragment(element["name"], element["representedBy"])
                self.fragments.append(fragment)
            except:
                raise Exception("EmptyOptionalFragment")

        for sequence_diagram in diagram["SequenceDiagrams"]:
            try:            
                elements=[]
                for element in sequence_diagram["elements"]:

                    if element["type"] == "Fragment":
                        node=FragmentReference(element["name"])
                        elements.append(node)

                    if element["type"] == "Message":
                        try:
                            node=Message(element["name"], element["message_type"], element["prob"], element["source"], element["target"])
                            elements.append(node)
                        except:
                            raise Exception("MessageFormatException")
                
                this_diagram=SequenceDiagram(sequence_diagram["name"], sequence_diagram["guard_condition"], elements)
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
            print('\t\t<Optional name="{}" representedBy="{}" />'.format(fragment.name, fragment.representedBy), file=file)
        print('\t</Fragments>', file=file)
        for diagram in self.diagrams:
            print('\t<SequenceDiagram name="{}" guardCondition="{}">'.format(diagram.name, diagram.guard_condition), file=file)
            for element in diagram.elements:
                if element.type == 'Message':   
                    print('\t\t<Message type="{}" name="{}" prob="{}" source="{}" target="{}" />'.format(element.message_type, element.name, element.prob, element.source, element.target), file=file)
                else:
                    print('\t\t<Fragment name="{}" />'.format(element.name), file=file)

            print('\t</SequenceDiagram>', file=file)
        print('<SequenceDiagrams>', file=file)


