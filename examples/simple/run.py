from examples.simple.module_a import ModuleA
from examples.simple.module_b import ModuleB


def run():
    module_a = ModuleA()
    module_a.add(ModuleB())

    module_a.start()


if __name__ == '__main__':
    run()
