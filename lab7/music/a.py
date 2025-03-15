import pygame
import os
pygame.init()
done = False
playlist = []
# Папка с музыкой
music_folder = r"C:\Users\Acer Aspire Lite\pp2\labs_pp2\lab7\music\musics"
allmusc = os.listdir(music_folder)
for song in allmusc:
    if song.endswith(".mp3"):  # Добавляем только mp3-файлы
        playlist.append(os.path.join(music_folder, song))

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("My Playlist")
clock = pygame.time.Clock()
background = pygame.image.load(os.path.join("lab7", "music", "elements", "background.png")) #фон
bg = pygame.Surface((500, 200))
bg.fill((255, 255, 255))
# Шрифты
font2 = pygame.font.SysFont("timesnewroman", 25)
# Кнопки управления
play_img = pygame.image.load(os.path.join("lab7", "music", "elements", "play.png"))
pause_img = pygame.image.load(os.path.join("lab7", "music", "elements", "pause.png"))
next_img = pygame.image.load(os.path.join("lab7", "music", "elements", "next.png"))
prev_img = pygame.image.load(os.path.join("lab7", "music", "elements", "back.png"))
# Масштаб
play_scaled = pygame.transform.scale(play_img, (70, 70))
pause_scaled = pygame.transform.scale(pause_img, (70, 70))
next_scaled = pygame.transform.scale(next_img, (70, 70))
prev_scaled = pygame.transform.scale(prev_img, (75, 75))
index = 0
pygame.mixer.music.load(playlist[index])
pygame.mixer.music.play(-1)  # Бесконечное воспроизведение
audio_playing = True 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Пауза/воспроизведение
                if audio_playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                audio_playing = not audio_playing

            if event.key == pygame.K_RIGHT:  # Следующий трек
                index = (index + 1) % len(playlist)
                pygame.mixer.music.stop()
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play(-1)

            if event.key == pygame.K_LEFT:  # Предыдущий трек
                index = (index - 1) % len(playlist)
                pygame.mixer.music.stop()
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play(-1)

            if event.key == pygame.K_s:  # Остановить воспроизведение
                pygame.mixer.music.stop()
                audio_playing = False
    screen.blit(background, (-50, 0))
    screen.blit(bg, (155, 500))
    text2 = font2.render(os.path.basename(playlist[index]), True, (20, 20, 50))
    screen.blit(text2, (300, 525))
    if audio_playing:
        screen.blit(pause_scaled, (370, 590))
    else:
        screen.blit(play_scaled, (370, 590))
    
    screen.blit(next_scaled, (460, 587))
    screen.blit(prev_scaled, (273, 585))

    pygame.display.set_caption(f"Now Playing: {os.path.basename(playlist[index])}")
    
    clock.tick(24)
    pygame.display.update()

pygame.quit()
