import os
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)

from diagrams.activity_diagram import Node, StartNode, Activity, DecisionNode, MergeNode, Transition, ActivityDiagram, FinalNode
from diagrams.sequence_diagrams import SequenceElement, Fragment, Lifeline, SequenceDiagrams, SequenceDiagram, Message, FragmentReference, SequenceDiagrams
import index

class TestProject:
    def test_falsificacao(self):
        entrada = "<ActivityDiagram name='nome_diagrama'>"
        saida = "</ActivityDiagram>"
        xml = entrada + saida
        assert (entrada == "<ActivityDiagram name='nome_diagrama'>" )
        assert (saida == "</ActivityDiagram>")
        assert (xml == "<ActivityDiagram name='nome_diagrama'></ActivityDiagram>")

    def test_dict(self):
        assert type(index.dict_activity_diagram) is dict

# testes diagrama de atividades
    def test_node(self):
        node = Node("node 1")
        assert(node.name == "node 1")
        assert(node.type == '')
        assert(node.source_qtd == 0)
        assert(node.target_qtd == 0)
        assert(node.max_source == 0)
        assert(node.max_target == 0)
        assert(node.has_max_source == False)
        assert(node.has_max_target == False)

    def test_node(self):
        node = Node("node 2")
        assert(node.name == "node 2")
        assert(node.type == '')
        assert(node.source_qtd == 0)
        assert(node.target_qtd == 0)
        assert(node.max_source == 0)
        assert(node.max_target == 0)
        assert(node.has_max_source == False)
        assert(node.has_max_target == False)

    def test_add_source_qtd(self):
        node = Node("node 1")
        node.add_source_qtd()
        assert(node.source_qtd == 1)
        node.add_source_qtd()
        assert(node.source_qtd == 2)
        node.add_source_qtd()
        assert(node.source_qtd == 3)
        
    def test_add_target_qtd(self):
        node = Node("node 1")
        node.add_target_qtd()
        assert(node.target_qtd == 1)
        node.add_target_qtd()
        assert(node.target_qtd == 2)
        node.add_target_qtd()
        assert(node.target_qtd == 3)

    def test_start_node(self):
        node = StartNode("Start Node")
        assert(node.name == "Start Node")
        assert(node.type == 'StartNode')
        assert(node.has_max_target==True)
        assert(node.has_max_source==True)
        assert(node.max_source==1)
        assert(node.source_qtd == 0)
        assert(node.target_qtd == 0)
        assert(node.max_target == 0)

    def test_activity(self):
        node = Activity("Activity Node")
        assert(node.name == "Activity Node")
        assert(node.type == 'Activity')
        assert(node.has_max_target==True)
        assert(node.max_target==1)
        assert(node.has_max_source==True)
        assert(node.max_source==1)
        assert(node.source_qtd == 0)
        assert(node.target_qtd == 0)

    def test_decision_node(self):
        node = DecisionNode("Decision Node")
        assert(node.name == "Decision Node")
        assert(node.type == 'DecisionNode')
        assert(node.has_max_target==True)
        assert(node.max_target==1)
        assert(node.source_qtd == 0)
        assert(node.target_qtd == 0)
        assert(node.max_source == 0)
        assert(node.has_max_source == False)

    def test_merge_node(self):
        node = MergeNode("Merge Node")
        assert(node.name == "Merge Node")
        assert(node.type == 'MergeNode')
        assert(node.has_max_source==True)
        assert(node.max_source==1)
        assert(node.source_qtd == 0)
        assert(node.target_qtd == 0)
        assert(node.max_target == 0)
        assert(node.has_max_target == False)

    def test_final_node(self):
        node = FinalNode("Final Node")
        assert(node.name == "Final Node")
        assert(node.type == 'FinalNode')
        assert(node.has_max_source==True)
        assert(node.max_source==0)
        assert(node.source_qtd == 0)
        assert(node.target_qtd == 0)
        assert(node.max_target == 1)
        assert(node.has_max_target == True)

    def test_transition(self):
        transition = Transition("transition name", 1, "source name", "target name")
        assert(transition.name == "transition name")
        assert(transition.prob == 1)
        assert(transition.source == "source name")
        assert(transition.target == "target name")

    def test_activity_diagram(self):
        activityDiagrams = ActivityDiagram(index.dict_activity_diagram)
        assert(activityDiagrams.has_start_node == True)
        assert(activityDiagrams.has_final_node == True)
        assert(len(activityDiagrams.elements) == 6)
        assert(len(activityDiagrams.transitions) == 1)
        assert(len(activityDiagrams.getElements()) == 6)

#testes diagrama de sequencia
    def test_sequence_element(self):
        sequenceElement = SequenceElement("sequence element name")
        assert(sequenceElement.name == "sequence element name")
        assert(sequenceElement.type == '')

    def test_fragment(self):
        fragment = Fragment("fragment name", "representation")
        assert(fragment.name == "fragment name")
        assert(fragment.representedBy == "representation")

    def test_fragment_reference(self):
        fragment = FragmentReference("Fragment")
        assert(fragment.type == "Fragment")

    def test_lifeline(self):
        lifeline = Lifeline("lifeline")
        assert(lifeline.name == "lifeline")

    def test_message(self):
        message = Message("message name", "sync", 1, "source message", "target message")
        assert(message.name == "message name")
        assert(message.message_type == "sync")
        assert(message.prob == 1)
        assert(message.source == "source message")
        assert(message.target == "target message")

    def test_sequence_diagram(self):
        sequenceDiagram = SequenceDiagram("sequence diagram name", "guard condition", "elements")
        assert(sequenceDiagram.name == "sequence diagram name")
        assert(sequenceDiagram.guard_condition == "guard condition")
        assert(sequenceDiagram.elements == "elements")

    def test_file_exist(self):
        file = os.path.exists("diagrams.xml")
        assert(file)

    def test_sequence_diagrams(self):
        sequenceDiagrams = SequenceDiagrams(index.dict_sequence_diagram)
        assert(len(sequenceDiagrams.lifelines) == 3)
        assert(len(sequenceDiagrams.fragments) == 3)
        assert(len(sequenceDiagrams.diagrams) == 2)
        assert(len(sequenceDiagrams.getDiagrams()) == 2)

    def test_activity_with_sequence_diagrams(self):
        activityDiagrams = ActivityDiagram(index.dict_activity_diagram)
        sequenceDiagrams = SequenceDiagrams(index.dict_sequence_diagram)
        with open('diagrams.xml', 'w+') as f:
            activityDiagrams.getXml(f)
            sequenceDiagrams.getXml(f)
        
        with open('diagrams.xml', 'r') as f:
            data=f.readlines()
            print(data)
            assert(len(data) == 37)
