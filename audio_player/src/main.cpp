#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <FL/Fl_Button.H>
#include <FL/Fl_Input.H>
#include <FL/Fl_Group.H>
#include <FL/Fl_Box.H>
#include <iostream>
#include "../include/SFML/Audio.hpp"

sf::SoundBuffer buffer;
sf::Sound sound;

void play_callback(Fl_Widget *widget, void *data) {
    Fl_Input *in = (Fl_Input *)data;

    if (in->value() != nullptr) {
        if (!buffer.loadFromFile(in->value())) {
            std::cerr << "Failed to load audio file" << std::endl;
            return;
        }

        sound.setBuffer(buffer);

        if (sound.getStatus() != sf::Sound::Playing) {
            sound.play();
        }
    }
}

void pause_callback(Fl_Widget *widget, void *data) {
    if (sound.getStatus() == sf::Sound::Playing) {
        sound.stop();
    }
}

void reset_callback(Fl_Widget *widget, void *data) {
    sound.stop();
    sound.play();
}

int main(int argc, char **argv) {

    Fl_Window *window = new Fl_Window(330, 250, "FLTK Window");

    Fl_Group *group = new Fl_Group(0, 0, 330, 140);
    {
        Fl_Input *input = new Fl_Input(65 + 2, 50, 200, 30, "File Path: ");

        Fl_Button *play = new Fl_Button(30, 90, 80, 40, "Play");
        Fl_Button *pause = new Fl_Button(130, 90, 80, 40, "Pause");
        Fl_Button *reset = new Fl_Button(230, 90, 80, 40, "Reset");

        play->callback(play_callback, input);
        pause->callback(pause_callback, nullptr);
        reset->callback(reset_callback, nullptr);
    }

    group->end();

    window->end();
    window->show(argc, argv);

    return Fl::run();
}
