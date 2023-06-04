# ⬛️ Black Box: An Exploration of Authenticity, Influence, and Bias under the Transhumanist Era 🧠
Zeynep Toprakbasti's DXARTS 472 Mechatronics Art Spring 2023 Final Project
|||
:-------------------------:|:-------------------------:
|![](/images/desc.png)     |  ![](/images/setup1.png) | 

### Description
Within the scope of the class theme, "The Anthropocene, Transhumanism and Non-human entities", <em> Black Box </em> seeks to explore the implications of a world growing increasingly dependent on automation and big data in order to cultivate meaning in our lives. Black Box is a wire brain sculpture with independent regions that can light up depending on the logic inside the black box. Based on thousands of posts collected from the internet and sentiment analysis, the hidden algorithm inside the box, inspired by the notion of "black box ai", determines which part of the brain is most relevant in expressing the sentiment implied from a web-scraped piece of text. The text that the brain is currently thinking about is displayed on a monitor next to the sculpture so that the observers can read what the text is and see how the brain interprets its general sentiment. In accordance with the patterns that exist within this data, it is naturally observed that the regions most associated with depression, anxiety, anger, and fear light up in the brain the most. Howevever, <em> Black Box </em> also comes with a microphone and an infrared distance sensor, so that when it detects the presence of another human being, the entire sculpture lights up all together.

The intention of this work is to show the emptiness of an intelligence artificially constructed on biased data. It is a commentary on the shifting of values within our society and how we define "meaning" during and after the AI revolution. Under capitalism, technological development is always driven by profit. When profit is the goal, the tools, companions, relationships, ecosystems, and mental pictures we build optimize towards compartmentalized and narrow visions. Interdisciplinary thought as well as natural empathy is abandoned, as we seek to artificially recreate these concepts by means of a rigorous, digital colonization of the human mental landscape.

![](/images/setup.png) 

 <em> Black Box </em> seeks to hint at the following questions:

1. What happens when we try to artificially build personalities?
2. What do personalities look like when they are developed with the goal of profit?
3. What does authenticity look like in the age of big data and machine learning?
4. What are the consequences of digitally mimicking concepts that have been abandoned under capitalism and the patriarchy instead of seeking them out organically?
5. As a result, how do concepts like: creation, identity, and status manifest in the transhuman efforts to digitally mimic such ideas?

|Screenshot of Black Box program output  | 
|:-------------------------:|
|![](/images/sc1.png)  ![](/images/sc2.png)       |


### Research

 <em> Black Box </em> features a wire brain sculpture decomposed into 4 main parts: The right hemisphere (I), the brain stem (II), the amygdala(III), and the left hemisphere(IV). Each part is responsible for a set of emotions. In reality, this is not how the brain operates; all areas of the brain work together to serve a variety of functions. However, this project is a metaphor for how the modern approach to artificial intelligence seeks to compartmentlize its tasks without deeper motivation. So, the emotions that each part is responsible for can be thought of as an extreme simplification, or an artistic demonstration of a general idea. 


|I                           |  II                          | III                        | IV             |
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
|![](/images/left.png)  |  ![](/images/stem.png) |  ![](/images/amy.png)     |  ![](/images/right.png) |




 While recent studies show that certain tasks can be sourced to specific regions of the brain, the notion that the left brain is responsible for logic and the right brain responsible for art is largely a myth. People's personalities or strengths cannot be attributed to the dominance of a single hemisphere over the other. Rather, specific tasks can be sourced to specific sets of regions within the brain as a whole (Shmerling, 2022). Thus, it is important for all humans to value all different parts of the strengths they have in their ways of thinking.

 In this project, the regions are assigned to emotional themes as follows:
 

 * (I) The right hemisphere is associated with depressive emotions, as a hyper demonstrated in Li et. al., (2018) and Hecht (2010).
 * (II) The brainstem is associated with neutral emotions, as it has been shown to play a role in evaluating sensory information (Venkatraman et. al., 2017).
 * (III) The amygdala is associated with anger, fear, and anxiety as it is responsible for threat assessment (Adams et. al. 2003)
*  (IV) The left hemisphere is associated with the more positive emotions.


### To Run
Assemble Arduino circuitry as shown below  using the Arduino microphone and IR sensor. In place of the LEDs in the diagram, attach the positive side of the brain sections to the corresponding pins. Upload the code file to the Arduino or upload the `StandardFirmata.ino` code from the Arduino library. Finally, run the `/python/arduino_firmata_script.py` script.

<img src="/arduino/final_schematic.png"  width="600">

### Dataset
The dataset used for this project was collected from multiple sources on Kaggle.com


### Process
For the software, this project consisted of putting together a script that synthesizes multiple data sources and merges different posts of similar sentiment.  For the hardware, the piece consists of a wire brain scultpture and an acrylic black box. The box was built using a laser cutter,  acrylic glue, and fabric to secure the interactive sensors. The brain sculpture was hand molded with electronic 18 AWG copper bus wire. The lights are SMB LEDs and were soldered onto the 18 AWG wire. Upon completion of the wire sculpture, the wires were consolidated inside of the box using heat shrink tubes and then connected to the rest of the circuitry.

<img align="right" src="/images/closeup.png"  width="300">


### References
Adams RB;Gordon HL;Baird AA;Ambady N;Kleck RE; (2003, June 6). Effects of gaze on amygdala sensitivity to anger and fear faces. Science (New York, N.Y.). https://pubmed.ncbi.nlm.nih.gov/12791983/ 

D;, H. (2010, July 21). Depression and the hyperactive right-hemisphere. Neuroscience research. https://pubmed.ncbi.nlm.nih.gov/20603163/ 

Li, M., Xu, H., &amp; Lu, S. (2018, June 5). Neural basis of depression related to a dominant right hemisphere: A resting-state fmri study. Behavioural neurology. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6008682/ 

Robert H. Shmerling, M. (2022, March 24). Right brain/left brain, right?. Harvard Health. https://www.health.harvard.edu/blog/right-brainleft-brain-right-2017082512222 

Venkatraman, A., Edlow, B. L., &amp; Immordino-Yang, M. H. (2017, February 20). The brainstem in Emotion: A review. Frontiers. https://www.frontiersin.org/articles/10.3389/fnana.2017.00015/full 

