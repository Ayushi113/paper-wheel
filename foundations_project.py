# -*- coding: UTF-8 -*-
from turtle import Turtle, Screen
import turtle, math
import sys
sys.stderr.write("\x1b[2J\x1b[H")
author_list = { "1)": "NOAM CHOMSKY 1965", "2)": "FODOR & PYLYSHYN", "3)": "MICHAEL MCCLOSKEY", "4)":'NEWELL & SIMON', '5)': 'LOCKE in RUSSELL' , '6)': 'DONALD O. HEBB' , '7)': 'DAVID MARR', '8)': 'SMOLENSKY & LEGENDRE', '9)': 'GARY MARCUS', '10)' : 'RUMELHART & MCLELLAND', '11)': 'JOHN SEARLE', '12)' : "ARISTOTLE in RUSSELL"}


print "*" * 182
print "\n\n\n"

print " " * 100, "Welcome"
print "\n\n\n"

print " " * 25, "We are covering:-"
print " " * 55, "1) Noam Chomsky (1965) \t\t\t 2) Fodor and Pylyshyn\n"
print " " * 55, "3) Michael McCloskey \t\t\t 4) Newell and Simon \n"
print " " * 55, "5) Locke in Russell \t\t\t 6) Hebb\n"
print " " * 55, "7) David Marr \t\t\t\t 8) Smolensky and Legendre\n"
print " " * 55, "9) Gary Marcus \t\t\t\t 10) Rumelhart and McLelland\n"
print " " * 55, "11) John Searle \t\t\t 12) Aristotle in Russell\n"

print " " * 25, ".....over 7 course issues:-"
print " " * 55, "[Theories]\n"
print " " * 55, "[Representational]\n"
print " " * 55, "[Knowledge]\n"
print " " * 55, "[Levels]\n"
print " " * 55, "[Computational]\n"
print " " * 55, "[Processor]\n"



print "*" * 182

A1 = raw_input("Who would you like your three authors to be?\n")

authors= A1.split(', ')
print "\n"

print "Your authors are:\n", authors[0], author_list[authors[0]], '\n', authors[1], author_list[authors[1]], '\n', authors[2], author_list[authors[2]]

print "\n"

c_issue = raw_input("What is the course issue you want to see across these authors?\n")
print "Your course issue is:", c_issue

RADIUS = 100

def connect_nodes(turtle, p, q, verd):
    if verd == 'yes':
       for i in p:
           turtle.goto(i[0], i[1])
           turtle.color("black")
           turtle.down()
           turtle.pensize(3)
           turtle.goto(0,0)

           for j in q:
               turtle.goto(j[0], j[1]+2*RADIUS)
               turtle.up()

    elif verd == 'no':
       for i in p:
           if i == (0,0):
              turtle.up()
           else:
              turtle.goto(i[0], i[1])
              for j in q:
                  print j
                  if j == (0, 0):
                     turtle.up()
                  else:
                     turtle.color("black")
                     turtle.down()
                     turtle.pensize(3)
                     turtle.goto(j[0], j[1]+2*RADIUS)

                  turtle.up()
                  turtle.goto(i[0], i[1])
           turtle.up()
           turtle.color("blue")


def draw_first(turtle, text, x, y, cl):
    turtle.up()
    turtle.goto(x, y- RADIUS)
   # print "I'm here!"
    turtle.color(cl)
    turtle.down()
    turtle.pensize(10)
    #turtle.begin_fill()
    turtle.circle(RADIUS)
    #turtle.end_fill()
   #turtle.shapetransform()
    turtle.up()
    turtle.goto(x, y-30)
    turtle.color("black")
    turtle.pensize(3)
    turtle.write(text, align="center", font=15)
    turtle.color("blue")
    turtle.pensize(3)



def draw_node(turtle, text, x, y, cl):
    turtle.up()
    turtle.goto(x, y- RADIUS)
   # print "I'm here!"
    turtle.color(cl)
    turtle.down()
    turtle.pensize(10)
    #turtle.begin_fill()
    turtle.circle(RADIUS)
    #turtle.end_fill()
   #turtle.shapetransform()
    turtle.up()
    turtle.goto(x, y-(RADIUS*0.7))
    turtle.color("black")
    turtle.pensize(3)
    turtle.write(text, align="center", font=FONT)
    turtle.color("blue")
    turtle.pensize(3)


FONT_SIZE = 8
screen = turtle.Screen()
screen.setup(2000,2000)
FONT = ("monaco", FONT_SIZE, "normal")

def draw_design(turtle, author, text_list, tht, x, y):
    CI_positions = []
    text_list_positions = []
    CI_position = (0, 0)
    turtle.color("blue")
    turtle.pensize(10)
    col = 'black'
    
    draw_first(turtle, author, x, y, col)
    
    turtle.goto(x+RADIUS, y)
    turtle.down()
    turtle.left(tht)
    turtle.forward(120)

    #dashed_line(turtle, 5)
    turtle.up()
    turtle.right(tht)
    col = ''
    #k = turtle.pos()
    for i in text_list:
      if i.endswith("[Computational]"):
         col = "gold"
         CI = '[Computational]'
         if c_issue.endswith("[Computational]"):
            CI_position = turtle.pos()
            P = CI_position[0]+RADIUS
            Q = CI_position[1]-RADIUS
            CI_position = (P, Q)
            CI_positions.append(CI_position)
         
      elif i.endswith("[Levels]"):
         col = "green"
         CI = '[Levels]'
         if c_issue.endswith("[Levels]"):
            CI_position = turtle.pos()
            P = CI_position[0]+RADIUS
            Q = CI_position[1]-RADIUS
            CI_position = (P, Q)
            CI_positions.append(CI_position)
         
      elif i.endswith("[Theories]"):
         col = "medium orchid"
         CI = '[Theories]'
         if c_issue.endswith("[Theories]"):
            CI_position = turtle.pos()
            P = CI_position[0]+RADIUS
            Q = CI_position[1]-RADIUS
            CI_position = (P, Q)
            CI_positions.append(CI_position)
         
      elif i.endswith("[Representational]"):
         col = "crimson"
         CI = '[Representational]'
         if c_issue.endswith("[Representational]"):
            CI_position = turtle.pos()
            P = CI_position[0]+RADIUS
            Q = CI_position[1]-RADIUS
            CI_position = (P, Q)
            CI_positions.append(CI_position)
         
      elif i.endswith("[Processor]"):
         col = "pink"
         CI = '[Processor]'
         if c_issue.endswith("[Processor]"):
            CI_position = turtle.pos()
            P = CI_position[0]+RADIUS
            Q = CI_position[1]-RADIUS
            CI_position = (P, Q)
            CI_positions.append(CI_position)
         
      elif i.endswith("[Formal]"):
         col = "royal blue"
         CI = '[Formal]'
         if c_issue.endswith("[Formal]"):
            CI_position = turtle.pos()
            P = CI_position[0]+RADIUS
            Q = CI_position[1]-RADIUS
            CI_position = (P, Q)
            CI_positions.append(CI_position)
         
      elif i.endswith("[Knowledge]"):
         col = "orange"
         CI = '[Knowledge]'
         if c_issue.endswith("[Knowledge]"):
            CI_position = turtle.pos()
            P = CI_position[0]+RADIUS
            Q = CI_position[1]-RADIUS
            CI_position = (P, Q)
            CI_positions.append(CI_position)

      else:
            continue
         

      k = turtle.pos()
      draw_node(turtle, i, k[0]+RADIUS, k[1], col)
      P = k[0]
      Q = k[1]
      text_list_positions.append((P, Q))
      turtle.goto(k[0]+2*RADIUS, k[1])
      turtle.down()
      if i == text_list[-1]:
         continue
         #turtle.forward(75)
         
         #turtle.up()
      else:
         #continue
         turtle.forward(90)
         turtle.up()
   
    m = turtle.pos()
    turtle.goto(m[0], m[1])
    turtle.down()
    turtle.right(tht)
    #turtle.forward(90)
   # dashed_line(turtle, 5)
    turtle.up()
    turtle.left(tht)
    return CI_positions, CI
    
screen = Screen()

yertle = Turtle(shape="arrow")
yertle.speed(0)

#1.
chomsky_65 = ['A theory of\nlinguistic\nstructure must\nhave explanatory\nand descriptive\nadequacy.\n[Formal]', 'Goal is to\nunderstand and\ncharacterize\nsimilarities\nacross human\nlanguages; what\ndoes the child\nbring to the lg\nlearning process?\n[Knowledge]', 'We must differ-\nentiate theories\nof lx structure\nthat describe\ndata only by ad\nhoc means from\nthose based on\nempirical\nassumptions.\n[Theories]', 'The underlying\nsystem of rules\n(competence) is\ndetermined\nthrough\nperformance.\n[Knowledge]', 'Linguistic\nuniversals are\nformal (grammar\nmeets certain\nabstract\nconditions) and\nsubstantive\n(fixed class of\nitems).\n[Levels]']
#2.
fodor_pylyshyn = ['Representational\nstates are\nessential to a\ntheory of\ncognition.\n[Representational]', 'Identifying the\nlevel of\nanalysis is\nimportant for\nunderstanding\ncognitive\narchitecture.\n[Levels]', 'Classical, not\nconnectionist,\ntheories, can\nexplain the\nproductivity and\ncompositionality\nof cognition.\n[Theories]', 'Thought is\nsystematic:\nmental represen-\ntations have\ninternal\nstructure. Caus-\nal & structural\nrelations are\nsemantically\nevaluable.\n[Representational]', 'It\'s impossible\nto have both a\ncombinatorial\nrepresentational\nsystem and a\nConnectionist\narchitecture at\nthe cognitive\nlevel.\n[Levels]']
#3.
mccloskey = ['Connectionist\nnetworks are not\n(yet) theories\nof cognitive\nfunctions or\neven simulations\nof theories.\n[Theories]', 'Theories are\nindependent of\nany particular\nmodel;\ninformativity of\nconnectionist\nnetworks is\nmostly limited\nto the phenomena\nthey model.\n[Levels]', 'Theories\nsupport\nclear-cut credit\nand blame\nassignment, and\nmake specific\nassumptions and\npredictions.\n[Formal]', 'When theories\nare clearly def-\nined we can id-\nentify how they\nare similar or\ndifferent;\nconnectionist\nmodels are hard\nto interpret.\n[Theories]', 'In studying\nconnectionist\nmodels, we must\nhave ideas about\nhow the model\ncorresponds to\nthe human system.\n[Levels]']
#4.
newell_simon = ['Humans are\nrepresentable as\ninformation\nprocessing\nsystems (IPS).\n[Theories]', 'The units of\ninformation in\nan IPS are\nsymbols and\nstructures of\nsymbols, which\nare potentially\ninfinite.\n[Representational]', 'Cognition is\nserial\ncomputation over\nsymbols, using\nspecific\nalgorithms.\n[Computational]', 'The set of\nknowledge states\nis generated\nfrom a finite\nset of objects,\nrelations,\nproperties, etc.\n[Knowledge]', 'External and\ninternal\nstructures are\nat least\npartially\nisomorphic.\n[Representational]']
#5.
locke = ['Ideas are the\nonly immediate\nobjects of the\nmind. Cognitive\nscience may be\nsaid to be the\nscience of\nmental knowledge\n[Theories]', 'Cognitive\nphenomenon may\nbe explained at\na highly\nabstract level—-\nat the level of\nideas and\noperations on\nideas\n[Levels]', 'Ideas may be\noperated on in\nthe mind—-\nknowledge arises\nfrom the\nperception of\nthe agreement or\ndisagreement of\ntwoideas\n[Computational]', 'Sensations have\nexternal causes,\n and resemble\n external causes\n in somerespects\n[Representational]', 'Mind may be\nviewed as device\nfor processing\nstructured\ninformation—-\nconsisting of\nsensation,\nsimple ideas\ncomplex ideas\n[Processor]']
#6.
hebb = ['Psychology and\nneurophysiology\n(theories of\nmental knowledge\n&brainfunction)\ncomplement each\nother as\nstudies of\ncognition\n[Theories]', 'Behaviors are\nproduced by\nactivities of\nnerve cells.\nFruitful\nexplanations of\ncognition lie\nat the level of\nneurons\n[Levels]', 'Cell assemblies\nhave distributed\nform of\nrepresentations,\nbut of the\nswitchboard\nvariety rather\nthan the field\ntheory variety\n[Processor]', '‘Representation’\narises from\nactivities of\ncell assemblies—\nnetworks of\nself-reinforcing\nneurons\n[Representational]', 'Psychological\nknowledge is\nimplicitly\nencoded in a\nlarge network of\nself-reinforcing\nneurons\n[Knowledge]']
#7.
marr =['Cognition may be\nstudied at brain\nfunction\n (hardware level)\nmental knowledge\n(algorithm), or\nbehavioral\n(computational\ngoal)\n[Theories]', 'Explanation of\ncognition may be\nconducted at 3\nindependent\nlevels—-\ncomputational,\nalgorithm, and\nhardware level\n[Levels]', 'Representation\nis a formal\nsystem for\nmaking explicit\na type of\ninformation\n[Formal]', 'At the algorithm\nlevel, the mind\nprocesses\nrepresentations\naccording to\nclearly laid out\nrules and\nalgorithms\n[Computational]', 'The mind employs\nrepresentations.\nChoices of\nrepresentations\nare constrained by factors\nsuch as choices\nof algorithms\n[Representational]']
#8.
smolensky_legendre = ['Cognition is\nunderstood as a\nscience of both\n(connectionist)\nbrain function\nand (symbolic\nstructure)\nmental knowledge\n[Theories]', 'Like structure\nof gas, mind can\nbe described at\neither coarse-\ngrained or fine-\ngrained level\n(computation of\ndiscrete symbols\n/numerical units\n[Levels]', 'According to ICS\nHarmonic Grammar\nand Optimality\nTheories provide\nformal\ndescriptions of\nthe mind at two\nindependent levels\n[Formal]', 'Representations\nare decomposed\ninto both\ndiscrete\n constituents\n(function level)\nand activation\nvalues (process\nlevel)\n[Representational]', 'Mind is both \nmassive parallel\nnumerical\nprocessing\n computer and\nsymbolicrule-\ngoverned\nmanipulation of\ndiscrete symbols\n[Processor]']
#9.
marcus = ['AI should have\n innate machinery\nsuch as object\nrepresentations,\nstructured\nalgebraic\nrepresentations,\noperations over\nvariables\n[Formal]', 'Innateness was\ndefined as a\nfunction of\nalgorithm,\nrepresentational\nformat,\nknowledge and\nexperience\n[Computational]', 'DNNs softwares\nsuch as AlphaGo\nwere created\nwith explicit\nknowledge about\ngame rules of AI\nprogrammers—-\nprofessional\ngame players\n[Representational]', 'Some board game\nsoftwares use\nMonte Carlo tree\nsearch mechanism\n, thusthey have\nboth innate\nalgorithms and\nrepresentation\nformat\n[Representational]', 'AI game programs\nare claimed to\nbe tabula rasa.\nHowever, they\noften possess\ninnate knowledge\nof game rules,\nboard structure,\netc.\n[Knowledge]']
#10.
rumelhart_mclelland = ['Cognition may be\nexplained at a\nhighly fine-\ngrained level—-\nunits and\ninteractions\nbetween units\n[Levels]', 'The foundational\n units of PDP\n representations\nare called\n‘wickelfeature’,\norcontext-\nsensitive\nphoneme units\n[Representational]', 'Mind is viewed\nas statistical\nprocessor—-\nlearning in PDP\nmodels occur via\nmodifications of\nconnection\nstrength\n[Processor]', 'Language\n acquisition is\nhandled by a\nmechanism with\nno explicit\nrepresentations\nof rules\n[Knowledge]', 'Performances of\nlanguage\nlearning device\n(e.g., PDP model\nof past-tense\nlearning) may be\ncharacterized by\nexplicit rules\n[Knowledge]']
#11.
searle = ['The ability to\nmanipulate\nformal symbols\ndoes not entail\nhaving an\nunderstanding of\nthose symbols.\n[Computational]', 'Intentionality\nand mental\nstates might be\ndependent on the\nstructure of the\nhuman brain.\n[Levels]', 'Intentional\nstates are\nincompatible\nwith formal\nmodels; thinking\ncannot be\nreplicated by a\nprogram.\n[Formal]', 'If a program\nonly simulates\nformal structure\nof neural pat-\nterns, it still\ndoesn’t simulate\nthe brain’s cap-\nacity to produce\nintentional\nstates.\n[Theories]', 'The relevant\nquestion is what\nis being\nattributed when\none attributes\ncognitive states\nto other people.\n[Knowledge]']
#12.
aristotle = ['All deductive\nreasoning is\nsyllogistic;\nvalid syllogisms\nmake it possible\nto avoid\nfallacies.\n[Formal]', 'Categories are\natomic entities,\nnot composed of\nother meaningful\nelements.\n[Representational]', 'Formal logic is\nessential to\nknowledge of the\nworld and mind.\n[Formal]', 'Essence is the\ninvariant nature\nof an entity -\nproperties that\ncannot be\nchanged without\nlosing its\nidentity.\n[Knowledge]', 'Substance exists\nindependently of\na subject, e.g.\ngrammatical\nknowledge in\none\'s mind.\n[Levels]']

author_names = { "1)": "NOAM CHOMSKY\n 1965", "2)": "FODOR\n &\n PYLYSHYN", "3)": "MICHAEL MCCLOSKEY", "4)":'NEWELL\n &\n SIMON', '5)': 'LOCKE in RUSSELL' , '6)': 'DONALD \n O. HEBB' , '7)': 'DAVID MARR', '8)': 'SMOLENSKY \n & \n LEGENDRE', '9)': 'GARY MARCUS', '10)' : 'RUMELHART\n & \n MCLELLAND', '11)': 'JOHN \n SEARLE', '12)' : "ARISTOTLE \n in RUSSELL"}
author_dict = { "1)": chomsky_65, "2)":fodor_pylyshyn, "3)":mccloskey, "4)":newell_simon, '5)': locke, '6)': hebb, '7)': marr, '8)':smolensky_legendre, '9)':marcus, '10)' : rumelhart_mclelland, '11)': searle, '12)' : aristotle}

positions = [(45, -750, 300), (0, -750, 0), (-45, -750, -300)]

author_positions = []
A_CIpos, issue = '', ''
subsetted_dic = {}
for at, pos in zip(authors, positions) :    
    for key, val in author_dict.items():
        if key == at:
           A_CIpos, issue = draw_design(yertle, author_names[key],  author_dict[key], pos[0], pos[1], pos[2])
           author_positions.append(A_CIpos)
           
        else:
           continue
if author_positions[1] == []:
   connect_nodes(yertle, author_positions[0], author_positions[2], 'yes')
else:
   connect_nodes(yertle, author_positions[0], author_positions[1], 'no')
   connect_nodes(yertle, author_positions[1], author_positions[2], 'no')


yertle.home()

screen.exitonclick()
