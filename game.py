from story.intro import Intro
from story.scenario_generator import ScenarioGenerator

character = Intro().executeModule()
ScenarioGenerator().generate(character)