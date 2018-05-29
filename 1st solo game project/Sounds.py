import pygame

def stop_channel(channel):
	pygame.mixer.Channel(channel).stop()

def channel_busy(channel):
	return True if pygame.mixer.Channel(channel).get_busy() else False

def play_head_hit():
	pygame.mixer.Channel(7).play(pygame.mixer.Sound("Sounds/Head_Bump.wav"))

def play_jump():
	pygame.mixer.Channel(6).play(pygame.mixer.Sound("Sounds/Jump.wav"))

def play_intro():
	pygame.mixer.Channel(1).play(pygame.mixer.Sound("Music/Intro_Song.wav"))

def play_slide():
	pygame.mixer.Channel(5).play(pygame.mixer.Sound("Sounds/Slide.wav"))