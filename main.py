from init import *
from images import *

#def showLevel():
#    screen.blit(levels[level_id-1]["questions"][question_id-1]["answers"][0]["text"], (0, 0))
#    screen.blit(levels[level_id-1]["questions"][question_id-1]["answers"][1]["text"], (0, 100))
#    screen.blit(levels[level_id-1]["questions"][question_id-1]["answers"][2]["text"], (0, 200))
#    screen.blit(levels[level_id-1]["questions"][question_id-1]["answers"][3]["text"], (0, 300))

#координаты, размер
#(252, 415, 390, 200)


#cub = pygame.Surface((60, 60))
#cub.fill((0, 255, 0))

def obdet():
    if lvL[1]["g"] == 0:
        le_yp[0] = 0
    elif lvL[1]["g"] == 1:
        le_yp[0] = 1
    elif lvL[1]["g"] > 1:
        le_yp[0] = 2
    
    if lvL[4]["g"] == 0:
        le_yp[2] = 0
    elif lvL[4]["g"] == 1:
        le_yp[2] = 1
    elif lvL[4]["g"] > 1:
        le_yp[2] = 2

    if lvL[2]["g"] == 0:
        le_yp[1] = 0
    elif lvL[2]["g"] == 1:
        le_yp[1] = 1
    elif lvL[3]["g"] > 1:
        le_yp[1] = 3
    elif lvL[2]["g"] > 1:
        le_yp[1] = 2

    if lvL[5]["g"] == 0:
        le_yp[3] = 0
    elif lvL[5]["g"] == 1:
        le_yp[3] = 1
    elif lvL[6]["g"] > 1:
        le_yp[3] = 3
    elif lvL[5]["g"] > 1:
        le_yp[3] = 2

    if lvL[7]["g"] == 0:
        le_yp[4] = 0
    elif lvL[7]["g"] == 1:
        le_yp[4] = 1
    elif lvL[9]["g"] > 1:
        le_yp[4] = 4
    elif lvL[8]["g"] > 1:
        le_yp[4] = 3
    elif lvL[7]["g"] > 1:
        le_yp[4] = 2



    if (X_L_1.collidepoint(m_p) and U_yp[0] < 4) or (X_L_1_p.collidepoint(m_p) and 4 > U_yp[0] > 0):
        U_yp[0] += 1
    elif not X_L_1_p.collidepoint(m_p) and U_yp[0] > 0:
        U_yp[0] -= 1
    if (X_L_2.collidepoint(m_p) and U_yp[1] < 4) or (X_L_2_p.collidepoint(m_p) and 4 > U_yp[1] > 0):
        U_yp[1] += 1
    elif not X_L_2_p.collidepoint(m_p) and U_yp[1] > 0:
        U_yp[1] -= 1
    if (X_L_3.collidepoint(m_p) and U_yp[2] < 4) or (X_L_3_p.collidepoint(m_p) and 4 > U_yp[2] > 0):
        U_yp[2] += 1
    elif not X_L_3_p.collidepoint(m_p) and U_yp[2] > 0:
        U_yp[2] -= 1
    if (X_L_4.collidepoint(m_p) and U_yp[3] < 4) or (X_L_4_p.collidepoint(m_p) and 4 > U_yp[3] > 0):
        U_yp[3] += 1
    elif not X_L_4_p.collidepoint(m_p) and U_yp[3] > 0:
        U_yp[3] -= 1
    if (X_L_5.collidepoint(m_p) and U_yp[4] < 4) or (X_L_5_p.collidepoint(m_p) and 4 > U_yp[4] > 0):
        U_yp[4] += 1
    elif not X_L_5_p.collidepoint(m_p) and U_yp[4] > 0:
        U_yp[4] -= 1
    if (X_L_6.collidepoint(m_p) and U_yp[5] < 4) or (X_L_6_p.collidepoint(m_p) and 4 > U_yp[5] > 0):
        U_yp[5] += 1
    elif not X_L_6_p.collidepoint(m_p) and U_yp[5] > 0:
        U_yp[5] -= 1
    if (X_L_7.collidepoint(m_p) and U_yp[6] < 4) or (X_L_7_p.collidepoint(m_p) and 4 > U_yp[6] > 0):
        U_yp[6] += 1
    elif not X_L_7_p.collidepoint(m_p) and U_yp[6] > 0:
        U_yp[6] -= 1
    if (X_L_8.collidepoint(m_p) and U_yp[7] < 4) or (X_L_8_p.collidepoint(m_p) and 4 > U_yp[7] > 0):
        U_yp[7] += 1
    elif not X_L_8_p.collidepoint(m_p) and U_yp[7] > 0:
        U_yp[7] -= 1
    if (X_L_9.collidepoint(m_p) and U_yp[8] < 4) or (X_L_9_p.collidepoint(m_p) and 4 > U_yp[8] > 0):
        U_yp[8] += 1
    elif not X_L_9_p.collidepoint(m_p) and U_yp[8] > 0:
        U_yp[8] -= 1
    if (X_L_10.collidepoint(m_p) and U_yp[9] < 4) or (X_L_10_p.collidepoint(m_p) and 4 > U_yp[9] > 0):
        U_yp[9] += 1
    elif not X_L_10_p.collidepoint(m_p) and U_yp[9] > 0:
        U_yp[9] -= 1

    if lvL[0]["g"] == 2 and lvL[0]["b"] == 5:
        lvL[0]["g"] = 3
    if lvL[1]["g"] == 0 and lvL[0]["g"] > 1:
        lvL[1]["g"] = 1
    if lvL[1]["g"] == 2 and lvL[1]["b"] == 5:
        lvL[1]["g"] = 3
    if lvL[2]["g"] == 0 and lvL[1]["g"] > 1:
        lvL[2]["g"] = 1
    if lvL[2]["g"] == 2 and lvL[2]["b"] == 5:
        lvL[2]["g"] = 3
    if lvL[3]["g"] == 0 and lvL[2]["g"] > 1:
        lvL[3]["g"] = 1
    if lvL[3]["g"] == 2 and lvL[3]["b"] == 5:
        lvL[3]["g"] = 3
    if lvL[4]["g"] == 0 and lvL[1]["g"] > 1:
        lvL[4]["g"] = 1
    if lvL[4]["g"] == 2 and lvL[4]["b"] == 5:
        lvL[4]["g"] = 3
    if lvL[5]["g"] == 0 and lvL[1]["g"] > 1:
        lvL[5]["g"] = 1
    if lvL[5]["g"] == 2 and lvL[5]["b"] == 5:
        lvL[5]["g"] = 3
    if lvL[6]["g"] == 0 and lvL[5]["g"] > 1:
        lvL[6]["g"] = 1
    if lvL[6]["g"] == 2 and lvL[6]["b"] == 5:
        lvL[6]["g"] = 3
    if lvL[7]["g"] == 0 and lvL[1]["g"] > 1:
        lvL[7]["g"] = 1
    if lvL[7]["g"] == 2 and lvL[7]["b"] == 5:
        lvL[7]["g"] = 3
    if lvL[8]["g"] == 0 and lvL[7]["g"] > 1:
        lvL[8]["g"] = 1
    if lvL[8]["g"] == 2 and lvL[8]["b"] == 5:
        lvL[8]["g"] = 3
    if lvL[9]["g"] == 0 and lvL[8]["g"] > 1:
        lvL[9]["g"] = 1
    if lvL[9]["g"] == 2 and lvL[9]["b"] == 5:
        lvL[9]["g"] = 3
def pocas(Y):
    global nV, lvl_komplit, lvl, nL, Fon, F_K
    if lvL[nL]["q"][nV - 1]["an"][Y]["cor"]:
        lvL_komplit[nV - 1] = 1
    else:
        lvL_komplit[nV - 1] = 0
    
    if nV > 4:
        if lvL_komplit[0] + lvL_komplit[1] + lvL_komplit[2] + lvL_komplit[3] + lvL_komplit[4] > lvL[nL]["b"]:
            lvL[nL]["b"] = lvL_komplit[0] + lvL_komplit[1] + lvL_komplit[2] + lvL_komplit[3] + lvL_komplit[4]
        if lvL[nL]["g"] == 1:
            lvL[nL]["g"] = 2
        lvL_komplit[0] = 3
        lvL_komplit[1] = 2
        lvL_komplit[2] = 2
        lvL_komplit[3] = 2
        lvL_komplit[4] = 2
        Fon = F_K
        nV = 1
    else:
        lvL_komplit[nV] = 3
        nV = nV + 1

        



go = True
while go: 

    keys = pygame.key.get_pressed()
    m_p = pygame.mouse.get_pos()

    screen.blit(Fon, (0, 0))

    #screen.blit(cub, (366, 225))

    obdet()

    if Fon == F_N:
        if X_K_nocl.collidepoint(m_p):
            screen.blit(K_nocl_p, (0, 0))
        else:
            screen.blit(K_nocl, (0, 0))
    elif Fon == F_K:
        screen.blit(le[0][le_yp[0]], (0, 0))
        screen.blit(le[1][le_yp[1]], (0, 0))
        screen.blit(le[2][le_yp[2]], (0, 0))
        screen.blit(le[3][le_yp[3]], (0, 0))
        screen.blit(le[4][le_yp[4]], (0, 0))


        if lvL[9]["g"] == 2 and U_yp[9] == 4: screen.blit(U_lev[lvL[9]["g"]][U_yp[9]][lvL[9]["b"]], (-190, -500))
        else: screen.blit(U_lev[lvL[9]["g"]][U_yp[9]], (-190, -500))
            
        if lvL[6]["g"] == 2 and U_yp[6] == 4: screen.blit(U_lev[lvL[6]["g"]][U_yp[6]][lvL[6]["b"]], (50, -460))
        else: screen.blit(U_lev[lvL[6]["g"]][U_yp[6]], (50, -460))
            
        if lvL[8]["g"] == 2 and U_yp[8] == 4: screen.blit(U_lev[lvL[8]["g"]][U_yp[8]][lvL[8]["b"]], (-200, -350))
        else: screen.blit(U_lev[lvL[8]["g"]][U_yp[8]], (-200, -350))
            
        if lvL[7]["g"] == 2 and U_yp[7] == 4: screen.blit(U_pra[lvL[7]["g"]][U_yp[7]][lvL[7]["b"]], (-184, -225))
        else: screen.blit(U_pra[lvL[7]["g"]][U_yp[7]], (-184, -225))
            
        if lvL[5]["g"] == 2 and U_yp[5] == 4: screen.blit(U_pra[lvL[5]["g"]][U_yp[5]][lvL[5]["b"]], (45, -210))
        else: screen.blit(U_pra[lvL[5]["g"]][U_yp[5]], (45, -210))
            
        if lvL[1]["g"] == 2 and U_yp[1] == 4: 
            screen.blit(U_lev[lvL[1]["g"]][U_yp[1]][lvL[1]["b"]], (119, -157))
        else: 
            screen.blit(U_lev[lvL[1]["g"]][U_yp[1]], (119, -157))
    
        if lvL[4]["g"] == 2 and U_yp[4] == 4: screen.blit(U_pra[lvL[4]["g"]][U_yp[4]][lvL[4]["b"]], (60, 0))
        else: screen.blit(U_pra[lvL[4]["g"]][U_yp[4]], (60, 0))
        
        if lvL[2]["g"] == 2 and U_yp[2] == 4: screen.blit(U_lev[lvL[2]["g"]][U_yp[2]][lvL[2]["b"]], (-170, -90))
        else: screen.blit(U_lev[lvL[2]["g"]][U_yp[2]], (-170, -90))
            
        if lvL[3]["g"] == 2 and U_yp[3] == 4: screen.blit(U_lev[lvL[3]["g"]][U_yp[3]][lvL[3]["b"]], (-125, -15))
        else: screen.blit(U_lev[lvL[3]["g"]][U_yp[3]], (-125, -15))
 
        if lvL[0]["g"] == 2 and U_yp[0] == 4: screen.blit(U_lev[lvL[0]["g"]][U_yp[0]][lvL[0]["b"]], (60, 50))
        else: screen.blit(U_lev[lvL[0]["g"]][U_yp[0]], (60, 50))
            
        if U_yp[9] == 4:
            screen.blit(lvL[9]["n"], (430, -25))
        if U_yp[6] == 4:
            screen.blit(lvL[6]["n"], (675, 15))
        if U_yp[8] == 4:
            screen.blit(lvL[8]["n"], (460, 125))
        if U_yp[7] == 4:
            screen.blit(lvL[7]["n"], (406, 175))
        if U_yp[5] == 4:
            screen.blit(lvL[5]["n"], (600, 190))
        if U_yp[1] == 4:
            screen.blit(lvL[1]["n"], (769, 318))
        if U_yp[4] == 4:
            screen.blit(lvL[4]["n"], (630, 400))
        if U_yp[2] == 4:
            screen.blit(lvL[2]["n"], (510, 385))
        if U_yp[3] == 4:
            screen.blit(lvL[3]["n"], (525, 460))
        if U_yp[0] == 4:
            screen.blit(lvL[0]["n"][0], (670, 510))
            screen.blit(lvL[0]["n"][1], (670, 535))






#        E = 0
#        for i in range(10):
#            if E == 7 or E == 4 or E == 5:
#                if lvL[E]["g"] == 2 and U_yp[E] == 4:
#                    screen.blit(U_pra[lvL[E]["g"]][U_yp[E]][lvL[E]["b"]], (nE[E][0], nE[E][1]))
#                else:
#                    screen.blit(U_pra[lvL[E]["g"]][U_yp[E]], (nE[E][0], nE[E][1]))
#            else:
#                if lvL[E]["g"] == 2:
#                    screen.blit(U_lev[lvL[E]["g"]][U_yp[E]][lvL[E]["b"]], (nE[E][0], nE[E][1]))
#                else:
#                    screen.blit(U_lev[lvL[E]["g"]][U_yp[E]], (nE[E][0], nE[E][1]))  
#            E += 1


        #screen.blit(U_lev[lvL[9]["g"]][U_yp[9]], (-190, -500))
        #screen.blit(U_lev[lvL[6]["g"]][U_yp[6]], (50, -460))
        #screen.blit(U_lev[lvL[8]["g"]][U_yp[8]], (-200, -350))
        #screen.blit(U_pra[lvL[7]["g"]][U_yp[7]], (-184, -225))
        #screen.blit(U_pra[lvL[5]["g"]][U_yp[5]], (45, -210))
        #screen.blit(U_lev[lvL[1]["g"]][U_yp[1]], (119, -157))
        #screen.blit(U_pra[lvL[4]["g"]][U_yp[4]], (60, 0))
        #screen.blit(U_lev[lvL[2]["g"]][U_yp[2]], (-170, -90))
        #screen.blit(U_lev[lvL[3]["g"]][U_yp[3]], (-125, -15))
        #screen.blit(U_lev[lvL[0]["g"]][U_yp[0]], (60, 60))



    






    if Fon == F_L_1 or Fon == F_L_2 or Fon == F_L_3 or Fon == F_L_4 or Fon == F_L_5 or Fon == F_L_6 or Fon == F_L_7 or Fon == F_L_8 or Fon == F_L_9 or Fon == F_L_10:

        if X_Con_a.collidepoint(m_p):
            screen.blit(Con_a_p, (0, 0))
            screen.blit(lvL[nL]["q"][nV - 1]["an"][0]["t"], (105, 55))
            screen.blit(lvL[nL]["q"][nV - 1]["an"][1]["t"], (90, 155))
            screen.blit(lvL[nL]["q"][nV - 1]["an"][2]["t"], (90, 255))
            screen.blit(lvL[nL]["q"][nV - 1]["an"][3]["t"], (90, 355))
        elif X_Con_b.collidepoint(m_p):
            screen.blit(Con_b_p, (0, 0))
            screen.blit(lvL[nL]["q"][nV - 1]["an"][0]["t"], (90, 55))
            screen.blit(lvL[nL]["q"][nV - 1]["an"][1]["t"], (105, 155))
            screen.blit(lvL[nL]["q"][nV - 1]["an"][2]["t"], (90, 255))
            screen.blit(lvL[nL]["q"][nV - 1]["an"][3]["t"], (90, 355))
        elif X_Con_c.collidepoint(m_p):
            screen.blit(Con_c_p, (0, 0))
            screen.blit(lvL[nL]["q"][nV - 1]["an"][0]["t"], (90, 55))
            screen.blit(lvL[nL]["q"][nV - 1]["an"][1]["t"], (90, 155))
            screen.blit(lvL[nL]["q"][nV - 1]["an"][2]["t"], (105, 255))
            screen.blit(lvL[nL]["q"][nV - 1]["an"][3]["t"], (90, 355))
        elif X_Con_d.collidepoint(m_p):
            screen.blit(Con_d_p, (0, 0))
            screen.blit(lvL[nL]["q"][nV - 1]["an"][0]["t"], (90, 55))
            screen.blit(lvL[nL]["q"][nV - 1]["an"][1]["t"], (90, 155))
            screen.blit(lvL[nL]["q"][nV - 1]["an"][2]["t"], (90, 255))
            screen.blit(lvL[nL]["q"][nV - 1]["an"][3]["t"], (105, 355))
        else:
            screen.blit(Con, (0, 0))
            screen.blit(lvL[nL]["q"][nV - 1]["an"][0]["t"], (90, 55))
            screen.blit(lvL[nL]["q"][nV - 1]["an"][1]["t"], (90, 155))
            screen.blit(lvL[nL]["q"][nV - 1]["an"][2]["t"], (90, 255))
            screen.blit(lvL[nL]["q"][nV - 1]["an"][3]["t"], (90, 355))

        screen.blit(Ben[lvL_komplit[0]], (0, 0))
        screen.blit(Ben[lvL_komplit[1]], (63, 0))
        screen.blit(Ben[lvL_komplit[2]], (126, 0))
        screen.blit(Ben[lvL_komplit[3]], (189, 0))
        screen.blit(Ben[lvL_komplit[4]], (252, 0))

        screen.blit(lvL[nL]["q"][nV - 1]["t"], (90, 550))

        if X_K_Krest.collidepoint(m_p):
            screen.blit(buk_p, (90, 550))
        else:
            screen.blit(buk, (90, 550))


    if Fon == F_L_P[0] or Fon == F_L_P[1] or Fon == F_L_P[2] or Fon == F_L_P[3] or Fon == F_L_P[4] or Fon == F_L_P[5] or Fon == F_L_P[6] or Fon == F_L_P[7] or Fon == F_L_P[8] or Fon == F_L_P[9]:
        if X_K_Krest.collidepoint(m_p):
            screen.blit(Krest_p, (90, 550))
        else:
            screen.blit(Krest, (90, 550))
        

    
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
        elif event.type == pygame.MOUSEBUTTONDOWN and X_K_nocl.collidepoint(m_p) and Fon == F_N:
            Fon = F_K
        elif event.type == pygame.MOUSEBUTTONDOWN and X_L_1_k.collidepoint(m_p) and U_yp[0] == 4 and Fon == F_K and lvL[0]["g"] > 0:
            Log_Fon = Fon
            Fon = F_L_P[0]
        elif event.type == pygame.MOUSEBUTTONDOWN and X_L_2_k.collidepoint(m_p) and U_yp[1] == 4 and Fon == F_K and lvL[1]["g"] > 0:
            Log_Fon = Fon
            Fon = F_L_P[1]
        elif event.type == pygame.MOUSEBUTTONDOWN and X_L_3_k.collidepoint(m_p) and U_yp[2] == 4 and Fon == F_K and lvL[2]["g"] > 0:
            Log_Fon = Fon
            Fon = F_L_P[2]
        elif event.type == pygame.MOUSEBUTTONDOWN and X_L_4_k.collidepoint(m_p) and U_yp[3] == 4 and Fon == F_K and lvL[3]["g"] > 0:
            Log_Fon = Fon
            Fon = F_L_P[3]
        elif event.type == pygame.MOUSEBUTTONDOWN and X_L_5_k.collidepoint(m_p) and U_yp[4] == 4 and Fon == F_K and lvL[4]["g"] > 0:
            Log_Fon = Fon
            Fon = F_L_P[4]
        elif event.type == pygame.MOUSEBUTTONDOWN and X_L_6_k.collidepoint(m_p) and U_yp[5] == 4 and Fon == F_K and lvL[5]["g"] > 0:
            Log_Fon = Fon
            Fon = F_L_P[5]
        elif event.type == pygame.MOUSEBUTTONDOWN and X_L_7_k.collidepoint(m_p) and U_yp[6] == 4 and Fon == F_K and lvL[6]["g"] > 0:
            Log_Fon = Fon
            Fon = F_L_P[6]
        elif event.type == pygame.MOUSEBUTTONDOWN and X_L_8_k.collidepoint(m_p) and U_yp[7] == 4 and Fon == F_K and lvL[7]["g"] > 0:
            Log_Fon = Fon
            Fon = F_L_P[7]
        elif event.type == pygame.MOUSEBUTTONDOWN and X_L_9_k.collidepoint(m_p) and U_yp[8] == 4 and Fon == F_K and lvL[8]["g"] > 0:
            Log_Fon = Fon
            Fon = F_L_P[8]
        elif event.type == pygame.MOUSEBUTTONDOWN and X_L_10_k.collidepoint(m_p) and U_yp[9] == 4 and Fon == F_K and lvL[9]["g"] > 0:
            Log_Fon = Fon
            Fon = F_L_P[9]
        elif event.type == pygame.MOUSEBUTTONDOWN and ((X_L_1_p.collidepoint(m_p) and U_yp[0] == 4) or (X_L_1.collidepoint(m_p) and U_yp[0] < 4)) and Fon == F_K and lvL[0]["g"] > 0:
            Fon = F_L_1
            nL = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and ((X_L_2_p.collidepoint(m_p) and U_yp[1] == 4) or (X_L_2.collidepoint(m_p) and U_yp[1] < 4)) and Fon == F_K and lvL[1]["g"] > 0:
            Fon = F_L_2
            nL = 1
        elif event.type == pygame.MOUSEBUTTONDOWN and ((X_L_3_p.collidepoint(m_p) and U_yp[2] == 4) or (X_L_3.collidepoint(m_p) and U_yp[2] < 4)) and Fon == F_K and lvL[2]["g"] > 0:
            Fon = F_L_3
            nL = 2
        elif event.type == pygame.MOUSEBUTTONDOWN and ((X_L_4_p.collidepoint(m_p) and U_yp[3] == 4) or (X_L_4.collidepoint(m_p) and U_yp[3] < 4)) and Fon == F_K and lvL[3]["g"] > 0:
            Fon = F_L_4
            nL = 3
        elif event.type == pygame.MOUSEBUTTONDOWN and ((X_L_5_p.collidepoint(m_p) and U_yp[4] == 4) or (X_L_5.collidepoint(m_p) and U_yp[4] < 4)) and Fon == F_K and lvL[4]["g"] > 0:
            Fon = F_L_5
            nL = 4
        elif event.type == pygame.MOUSEBUTTONDOWN and ((X_L_6_p.collidepoint(m_p) and U_yp[5] == 4) or (X_L_6.collidepoint(m_p) and U_yp[5] < 4)) and Fon == F_K and lvL[5]["g"] > 0:
            Fon = F_L_6
            nL = 5
        elif event.type == pygame.MOUSEBUTTONDOWN and ((X_L_7_p.collidepoint(m_p) and U_yp[6] == 4) or (X_L_7.collidepoint(m_p) and U_yp[6] < 4)) and Fon == F_K and lvL[6]["g"] > 0:
            Fon = F_L_7
            nL = 6
        elif event.type == pygame.MOUSEBUTTONDOWN and ((X_L_8_p.collidepoint(m_p) and U_yp[7] == 4) or (X_L_8.collidepoint(m_p) and U_yp[7] < 4)) and Fon == F_K and lvL[7]["g"] > 0:
            Fon = F_L_8
            nL = 7
        elif event.type == pygame.MOUSEBUTTONDOWN and ((X_L_9_p.collidepoint(m_p) and U_yp[8] == 4) or (X_L_9.collidepoint(m_p) and U_yp[8] < 4)) and Fon == F_K and lvL[8]["g"] > 0:
            Fon = F_L_9
            nL = 8
        elif event.type == pygame.MOUSEBUTTONDOWN and ((X_L_10_p.collidepoint(m_p) and U_yp[9] == 4) or (X_L_10.collidepoint(m_p) and U_yp[9] < 4)) and Fon == F_K and lvL[9]["g"] > 0:
            Fon = F_L_10
            nL = 9
        elif event.type == pygame.MOUSEBUTTONDOWN and X_Con_a.collidepoint(m_p) and (Fon == F_L_1 or Fon == F_L_2 or Fon == F_L_3 or Fon == F_L_4 or Fon == F_L_5 or Fon == F_L_6 or Fon == F_L_7 or Fon == F_L_8 or Fon == F_L_9 or Fon == F_L_10):
            pocas(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and X_Con_b.collidepoint(m_p) and (Fon == F_L_1 or Fon == F_L_2 or Fon == F_L_3 or Fon == F_L_4 or Fon == F_L_5 or Fon == F_L_6 or Fon == F_L_7 or Fon == F_L_8 or Fon == F_L_9 or Fon == F_L_10):
            pocas(1)
        elif event.type == pygame.MOUSEBUTTONDOWN and X_Con_c.collidepoint(m_p) and (Fon == F_L_1 or Fon == F_L_2 or Fon == F_L_3 or Fon == F_L_4 or Fon == F_L_5 or Fon == F_L_6 or Fon == F_L_7 or Fon == F_L_8 or Fon == F_L_9 or Fon == F_L_10):
            pocas(2)
        elif event.type == pygame.MOUSEBUTTONDOWN and X_Con_d.collidepoint(m_p) and (Fon == F_L_1 or Fon == F_L_2 or Fon == F_L_3 or Fon == F_L_4 or Fon == F_L_5 or Fon == F_L_6 or Fon == F_L_7 or Fon == F_L_8 or Fon == F_L_9 or Fon == F_L_10):
            pocas(3)
        elif event.type == pygame.MOUSEBUTTONDOWN and X_K_Krest.collidepoint(m_p) and (Fon == F_L_1 or Fon == F_L_2 or Fon == F_L_3 or Fon == F_L_4 or Fon == F_L_5 or Fon == F_L_6 or Fon == F_L_7 or Fon == F_L_8 or Fon == F_L_9 or Fon == F_L_10):
            Log_Fon = Fon
            Fon = F_L_P[nL]
        elif event.type == pygame.MOUSEBUTTONDOWN and X_K_Krest.collidepoint(m_p) and (Fon == F_L_P[0] or Fon == F_L_P[1] or Fon == F_L_P[2] or Fon == F_L_P[3] or Fon == F_L_P[4] or Fon == F_L_P[5] or Fon == F_L_P[6] or Fon == F_L_P[7] or Fon == F_L_P[8] or Fon == F_L_P[9]):
            Fon = Log_Fon

    clock.tick(30)
    pygame.display.update()

pygame.quit()      