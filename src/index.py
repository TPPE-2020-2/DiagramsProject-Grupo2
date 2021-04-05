import os
import sys

DIAGRAM_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(DIAGRAM_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)

from diagrams.activity_diagram import ActivityDiagram
from diagrams.sequence_diagrams import SequenceDiagrams

def diagram_tool(activity_diagram, sequence_diagrams):
  diagram1=ActivityDiagram(activity_diagram)
  diagram2=SequenceDiagrams(sequence_diagrams)

  elements=diagram1.getElements()
  diagrams=diagram2.getDiagrams()

  for element in elements:
      if element.type == 'Activity':
          found_diagram = False
          for diagram in diagrams:
              if diagram.name == element.name:
                  found_diagram = True
                  break
          
          if not found_diagram:
              raise Exception("ActivityRepresentationException")

  with open('diagrams.xml', 'w+') as f:
    diagram1.getXml(f)
    diagram2.getXml(f)


dict_activity_diagram = {
  "name": "test",
  "ActivityDiagramElements": [
    {
        "type": "StartNode",
        "name": "nome do start node"
    },
    {
        "type": "Activity",
        "name": "nome da atividade"
    },
    {
        "type": "Activity",
        "name": "nome da atividade 2"
    },
    {
        "type": "DecisionNode",
        "name": "nome do nodo de decisao"
    },
    {
        "type": "MergeNode",
        "name": "nome da atividade"
    },
    {
       "type": "FinalNode",
        "name": "nome do nodo final"
    },
  ],
  "ActivityDiagramTransitions": [
    {
      "name": "transition name",
      "prob": 1,
      "source": "nome do start node",
      "target": "nome da atividade"
    },
  ]
}

dict_sequence_diagram = {
    "Lifelines": [
        {
            "name": "nome da lifeline"
        },
        {
            "name": "nome da lifeline"
        },
        {
            "name": "nome da lifeline"
        }
    ],
    "Fagments": [
        {
            "type": "Opitional",
            "name": "nome do fragmento",
            "representedBy": "nome do diagrama de sequencia"
        },
        {
            "type": "Opitional",
            "name": "nome do fragmento",
            "representedBy": "nome do diagrama de sequencia"
        },
        {
            "type": "Opitional",
            "name": "nome do fragmento",
            "representedBy": "nome do diagrama de sequencia"
        }
    ],
    "SequenceDiagrams": [
      {
        "name": "nome da atividade",
        "guard_condition": "condição de guarda",
        "elements": [
            {
                "type": "Message",
                "message_type": "sync",
                "name": "nome da mensagem",
                "prob": "valor da probabilidade",
                "source": "nome da lifeline",
                "target": "nome da lifeline"
            },
            {
                "type": "Message",
                "message_type": "async",
                "name": "nome da mensagem",
                "prob": "valor da probabilidade",
                "source": "nome da lifeline",
                "target": "nome da lifeline"
            },
            {
                "type": "Fragment",
                "name": " nome do fragmento",
            },
            {
                "type": "Message",
                "message_type": "reply",
                "name": "nome da mensagem",
                "prob": "valor da probabilidade",
                "source": "nome da lifeline",
                "target": "nome da lifeline"
            }
        ],
      },
      {
        "name": "nome da atividade 2",
        "guard_condition": "condição de guarda",
        "elements": [
            {
                "type": "Message",
                "message_type": "sync",
                "name": "nome da mensagem",
                "prob": "valor da probabilidade",
                "source": "nome da lifeline",
                "target": "nome da lifeline"
            },
            {
                "type": "Message",
                "message_type": "async",
                "name": "nome da mensagem",
                "prob": "valor da probabilidade",
                "source": "nome da lifeline",
                "target": "nome da lifeline"
            },
            {
                "type": "Fragment",
                "name": " nome do fragmento",
            },
            {
                "type": "Message",
                "message_type": "reply",
                "name": "nome da mensagem",
                "prob": "valor da probabilidade",
                "source": "nome da lifeline",
                "target": "nome da lifeline"
            }
        ],
      },
    ]
}

diagram_tool(dict_activity_diagram, dict_sequence_diagram)
