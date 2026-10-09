"""ZOMBIE subset: entity declarations and the say, remember, moan and forget tasks.

Tasks run one after another instead of in threads, and no entity is ever
released into the outside world.
"""
import random
import re

from interpreters.common import out

DECLARATION = re.compile(r"^(\S+) is an? (.+)$", re.IGNORECASE)
TYPES = {
    "zombie": "zombie", "enslaved undead": "zombie", "ghost": "ghost", "restless undead": "ghost",
    "vampire": "vampire", "free-willed undead": "vampire", "demon": "demon", "djinn": "djinn",
}
TOKEN = re.compile(r'"([^"]*)"|(\S+)')


class Entity:
    def __init__(self, name, kind):
        self.name, self.kind = name, kind
        self.tasks, self.memory, self.active = [], None, kind not in ("zombie", "ghost")


def parse_zombie(source):
    entities, entity, task = {}, None, None
    for number, raw in enumerate(source.split("\n"), 1):
        line = raw.strip()
        word = line.lower()
        if not line:
            continue
        declaration = DECLARATION.match(line)
        if task is not None:
            if word in ("animate", "bind"):
                entity.tasks.append((task, word == "animate"))
                task = None
            else:
                task.append(line)
        elif declaration and entity is None:
            kind = TYPES.get(declaration.group(2).lower())
            if kind is None:
                raise SyntaxError(f"line {number}: unknown entity type {declaration.group(2)!r}")
            entity = entities[declaration.group(1)] = Entity(declaration.group(1), kind)
        elif entity is None:
            raise SyntaxError(f"line {number}: expected an entity declaration")
        elif word.startswith("task "):
            task = []
        elif word in ("animate", "bind", "disturb"):
            wakes = {"animate": "zombie", "disturb": "ghost"}.get(word)
            entity.active = entity.active or entity.kind == wakes
            entity = None
        elif word != "summon":
            raise SyntaxError(f"line {number}: unexpected statement {line!r}")
    if entity is not None or task is not None:
        raise SyntaxError("unfinished entity: a summon or task is missing its animate or bind")
    return entities


def combine(values):
    values = [v for v in values if v is not None]
    if all(isinstance(v, int) for v in values):
        return sum(values)
    return "".join(str(v) for v in values)


def run_statement(line, caller, entities):
    command, _, rest = line.partition(" ")
    # Arguments are evaluated from the end of the statement back to the start
    target, values = caller, []
    for string, word in reversed(TOKEN.findall(rest)):
        if word == "moan":
            values.append(target.memory)
            target = caller
        elif word in entities:
            target = entities[word]
        elif word:
            values.append(int(word))
        else:
            values.append(string)
    values.reverse()

    command = command.lower()
    if command == "say":
        out(f"{combine(values)}\n")
    elif command == "remember":
        target.memory = combine(values)
    elif command == "moan":
        out(f"{target.memory}\n")
    elif command == "forget":
        target.memory = None
    else:
        raise SyntaxError(f"unsupported task statement {line!r}")


def run_zombie(source):
    entities = parse_zombie(source)
    if not entities:
        raise SyntaxError("a ZOMBIE program must declare at least one entity")
    for entity in entities.values():
        if not entity.active:
            continue
        tasks = [statements for statements, active in entity.tasks if active]
        if entity.kind not in ("zombie", "ghost"):
            random.shuffle(tasks)
        for statements in tasks:
            for line in statements:
                run_statement(line, entity, entities)
