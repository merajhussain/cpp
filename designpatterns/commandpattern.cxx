#include <iostream>
#include <vector>
#include <memory>

// Command Interface
class Command {
public:
    virtual ~Command() = default;
    virtual void execute() = 0;
};

// Receiver
class Light {
public:
    void on() {
        std::cout << "Light is ON" << std::endl;
    }
    void off() {
        std::cout << "Light is OFF" << std::endl;
    }
};

// Concrete Command to turn the light on
class LightOnCommand : public Command {
private:
    Light& light;
public:
    LightOnCommand(Light& light) : light(light) {}
    void execute() override {
        light.on();
    }
};

// Concrete Command to turn the light off
class LightOffCommand : public Command {
private:
    Light& light;
public:
    LightOffCommand(Light& light) : light(light) {}
    void execute() override {
        light.off();
    }
};

// Invoker
class RemoteControl {
private:
    std::vector<std::unique_ptr<Command>> commands;
public:
    void addCommand(std::unique_ptr<Command> command) {
        commands.push_back(std::move(command));
    }
    void pressButton(int index) {
        if (index < commands.size()) {
            commands[index]->execute();
        }
    }
};

int main() {
    Light light;
    RemoteControl remote;
    remote.addCommand(std::make_unique<LightOnCommand>(light));
    remote.addCommand(std::make_unique<LightOffCommand>(light));

    remote.pressButton(0); // Light is ON
    remote.pressButton(1); // Light is OFF

    return 0;
}
