# Generated by OpenQL 0.11.1 for program example
version 1.2

pragma @ql.name("example")


.newKernel
    rz q[0], 4.290924898675601
    skip 1
    ry q[0], -2.761253373924344
    skip 1
    { # start at cycle 4
        rz q[0], 1.3952366566102345
        rz q[1], -1.3573296901778458
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], 1.3204498899128583
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], -0.21346663831465618
    skip 1
    ry q[0], -0.9150667812135661
    skip 1
    { # start at cycle 20
        rz q[0], 2.6132016895744994
        ry q[1], 2.1193723769271164
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    ry q[1], 0.6504638756652952
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 3.8439297490923345
    skip 1
    ry q[0], -2.3313155718254674
    skip 1
    { # start at cycle 36
        rz q[0], 0.8863566776626963
        rz q[1], 0.6178486929218577
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], -1.7802941257055378
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], -2.1886450197167546
    skip 1
    ry q[0], -1.2352690331131746
    skip 1
    { # start at cycle 52
        rz q[0], -0.9507516383922768
        rz q[2], -0.5716007742492423
    }
    skip 1
    cnot q[0], q[2]
    skip 3
    rz q[2], -1.6585479931579887
    skip 1
    cnot q[1], q[2]
    skip 3
    rz q[2], 0.8034172952664014
    skip 1
    cnot q[0], q[2]
    skip 3
    rz q[2], 0.07419285870866282
    skip 1
    { # start at cycle 72
        cnot q[1], q[2]
        rz q[0], 1.9831860963541172
    }
    skip 1
    ry q[0], -1.2647957586085963
    skip 1
    { # start at cycle 76
        rz q[0], -2.3703365503067606
        rz q[1], 2.1179173594934775
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], -0.8489510244043859
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], -3.6887136862883745
    skip 1
    ry q[0], -0.8200501174321576
    skip 1
    { # start at cycle 92
        rz q[0], -1.0284452679149474
        ry q[1], 1.8169289196292677
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    ry q[1], 0.9214852786492568
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], -4.056707287767269
    skip 1
    ry q[0], -2.3450128919079822
    skip 1
    { # start at cycle 108
        rz q[0], -1.7140046962118558
        rz q[1], -0.9366091924782675
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], -0.9949638493675832
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 5.6489981728629575
    skip 1
    ry q[0], -1.4153904960898285
    skip 1
    { # start at cycle 124
        rz q[0], 0.38182736716012045
        ry q[2], 1.467880080951839
    }
    skip 1
    cnot q[0], q[2]
    skip 3
    ry q[2], 0.46669570591890014
    skip 1
    cnot q[1], q[2]
    skip 3
    ry q[2], 0.0021353326394551453
    skip 1
    cnot q[0], q[2]
    skip 3
    ry q[2], 0.7092907200591816
    skip 1
    { # start at cycle 144
        cnot q[1], q[2]
        rz q[0], -2.3475386731052303
    }
    skip 1
    ry q[0], -1.5733186353005935
    skip 1
    { # start at cycle 148
        rz q[0], -2.912941018076074
        rz q[1], -0.1289967350949413
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], 0.992148754442061
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 1.6997930618898383
    skip 1
    ry q[0], -0.23062123118063924
    skip 1
    { # start at cycle 164
        rz q[0], 1.3445276066703666
        ry q[1], 1.9684246489172164
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    ry q[1], 0.38334519981464765
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 2.5167880517761243
    skip 1
    ry q[0], -1.2989452900192198
    skip 1
    { # start at cycle 180
        rz q[0], -1.0889811860810634
        rz q[1], -0.7051365411080446
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], 1.9385017788600265
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], -4.007252439276645
    skip 1
    ry q[0], -0.7640679432517145
    skip 1
    { # start at cycle 196
        rz q[0], 0.6749125479675486
        rz q[2], -0.10101062634921917
    }
    skip 1
    cnot q[0], q[2]
    skip 3
    rz q[2], -0.9672902281881579
    skip 1
    cnot q[1], q[2]
    skip 3
    rz q[2], -0.17105491662897854
    skip 1
    cnot q[0], q[2]
    skip 3
    rz q[2], 1.7113912357687324
    skip 1
    { # start at cycle 216
        cnot q[1], q[2]
        rz q[0], 1.3878392009247258
    }
    skip 1
    ry q[0], -1.1387283591412578
    skip 1
    { # start at cycle 220
        rz q[0], 0.13628317085351638
        rz q[1], -1.1571369790490995
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], 1.5146213147370475
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 2.727933305843996
    skip 1
    ry q[0], -1.3459253026312255
    skip 1
    { # start at cycle 236
        rz q[0], 1.433320896312536
        ry q[1], 0.9840636311180175
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    ry q[1], 0.43476501172001925
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], -4.6470608357300645
    skip 1
    ry q[0], -1.1514679627516617
    skip 1
    { # start at cycle 252
        rz q[0], 1.4139619943218649
        rz q[1], -0.5510858787277788
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], -1.8492098923489928
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 2.1218822055226756
    skip 1
    ry q[0], -1.4224654037387414
    skip 1
    { # start at cycle 268
        rz q[0], 3.720238079256889
        rz q[3], 0.03293356358216482
    }
    skip 1
    cnot q[0], q[3]
    skip 3
    rz q[3], 0.24237932560847894
    skip 1
    cnot q[1], q[3]
    skip 3
    rz q[3], 0.17810328301588516
    skip 1
    cnot q[0], q[3]
    skip 3
    rz q[3], 0.5677261943013256
    skip 1
    cnot q[2], q[3]
    skip 3
    rz q[3], 0.44315161288042626
    skip 1
    cnot q[0], q[3]
    skip 3
    rz q[3], -0.4863922975029519
    skip 1
    cnot q[1], q[3]
    skip 3
    rz q[3], -0.13304049075629557
    skip 1
    cnot q[0], q[3]
    skip 3
    rz q[0], -2.877784146572893
    skip 1
    ry q[0], -1.9513514439195287
    skip 1
    { # start at cycle 314
        rz q[0], 1.7399788381932209
        rz q[1], 0.9002081962166865
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], -0.5782391807390255
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 0.67058813057821
    skip 1
    ry q[0], -1.5030631068918505
    skip 1
    { # start at cycle 330
        rz q[0], 5.520666054293038
        ry q[1], 1.7788556076273425
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    ry q[1], 1.0847923325307798
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 2.868980672304242
    skip 1
    ry q[0], -0.9525600686314492
    skip 1
    { # start at cycle 346
        rz q[0], -2.0817115305931804
        rz q[1], -0.012012177245196203
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], 1.3925707209602967
    skip 1
    cnot q[0], q[1]
    skip 1
    rz q[3], -1.5769490747485682
    skip 1
    { # start at cycle 358
        cnot q[2], q[3]
        rz q[0], -4.700376803139493
    }
    skip 1
    ry q[0], -1.3240358866451003
    skip 1
    { # start at cycle 362
        rz q[0], 0.8502790977997994
        rz q[2], -0.4795008287728592
    }
    skip 1
    cnot q[0], q[2]
    skip 3
    rz q[2], -0.40617195143156737
    skip 1
    cnot q[1], q[2]
    skip 3
    rz q[2], -0.08318412882450343
    skip 1
    cnot q[0], q[2]
    skip 3
    rz q[2], 2.0104330013162874
    skip 1
    { # start at cycle 382
        cnot q[1], q[2]
        rz q[0], 1.976342189839935
    }
    skip 1
    ry q[0], -2.3220820998298057
    skip 1
    { # start at cycle 386
        rz q[0], -2.011581125394838
        rz q[1], -1.3484329587281472
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], -1.3196262054759722
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 2.9192292855230444
    skip 1
    ry q[0], -0.57702121403917
    skip 1
    { # start at cycle 402
        rz q[0], -1.1384060327612215
        ry q[1], 1.3749150567151731
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    ry q[1], 0.5163696169377922
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], -0.14517324482261074
    skip 1
    ry q[0], -0.49230352313971454
    skip 1
    { # start at cycle 418
        rz q[0], 0.18108096583121158
        rz q[1], 1.4609271606048286
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], 1.1303764629898876
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], -3.0317234873997254
    skip 1
    ry q[0], -1.523149843796359
    skip 1
    { # start at cycle 434
        rz q[0], 2.0988776590987444
        ry q[2], 1.4111344260553935
    }
    skip 1
    cnot q[0], q[2]
    skip 3
    ry q[2], 0.39390882175116176
    skip 1
    cnot q[1], q[2]
    skip 3
    ry q[2], 0.18224943523260362
    skip 1
    cnot q[0], q[2]
    skip 3
    ry q[2], 0.6130268828464196
    skip 1
    { # start at cycle 454
        cnot q[1], q[2]
        rz q[0], -3.823564525619928
    }
    skip 1
    ry q[0], -1.2185789131881555
    skip 1
    { # start at cycle 458
        rz q[0], -0.035588808788696635
        rz q[1], -0.9741184475343924
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], 1.63543722004165
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 2.5449147743292895
    skip 1
    ry q[0], -0.23301073489208546
    skip 1
    { # start at cycle 474
        rz q[0], 1.0315701969163094
        ry q[1], 1.6547250772824313
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    ry q[1], 0.9982329419156378
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], -1.0871201993025166
    skip 1
    ry q[0], -0.818707524125435
    skip 1
    { # start at cycle 490
        rz q[0], -5.0606240465174785
        rz q[1], -1.3997050479917272
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], -1.3711218488713384
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], -3.3126839323929627
    skip 1
    ry q[0], -1.4050862150381334
    skip 1
    { # start at cycle 506
        rz q[0], -0.054231142422287215
        rz q[2], 0.08381848713119067
    }
    skip 1
    cnot q[0], q[2]
    skip 3
    rz q[2], 0.3297789333901952
    skip 1
    cnot q[1], q[2]
    skip 3
    rz q[2], 0.6732562812867923
    skip 1
    cnot q[0], q[2]
    skip 3
    rz q[2], -1.8684616961072975
    skip 1
    { # start at cycle 526
        cnot q[1], q[2]
        rz q[0], -1.1045910059124466
    }
    skip 1
    ry q[0], -0.4801222714702859
    skip 1
    { # start at cycle 530
        rz q[0], -1.4801549912460774
        rz q[1], -0.6434578407048444
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], 0.699077238611724
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], -0.927338486090052
    skip 1
    ry q[0], -1.4727393546728542
    skip 1
    { # start at cycle 546
        rz q[0], -4.572471236469898
        ry q[1], 1.2087347240112398
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    ry q[1], 0.6816114991674554
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 1.3876809482007308
    skip 1
    ry q[0], -1.366747732373211
    skip 1
    { # start at cycle 562
        rz q[0], 0.5581453293415711
        rz q[1], -1.6233777080096976
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], 1.0325745332778542
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 0.05258138121480149
    skip 1
    ry q[0], -1.3026305667880524
    skip 1
    { # start at cycle 578
        rz q[0], -1.750633067904466
        ry q[3], 1.760977268489098
    }
    skip 1
    cnot q[0], q[3]
    skip 3
    ry q[3], 0.1496224791757997
    skip 1
    cnot q[1], q[3]
    skip 3
    ry q[3], 0.04083847206367348
    skip 1
    cnot q[0], q[3]
    skip 3
    ry q[3], 0.39254415058294606
    skip 1
    cnot q[2], q[3]
    skip 3
    ry q[3], -0.09255330942262928
    skip 1
    cnot q[0], q[3]
    skip 3
    ry q[3], -0.021244150764434946
    skip 1
    cnot q[1], q[3]
    skip 3
    ry q[3], -0.016201905460338877
    skip 1
    cnot q[0], q[3]
    skip 3
    rz q[0], 0.4742824905836396
    skip 1
    ry q[0], -2.4947617415608785
    skip 1
    { # start at cycle 624
        rz q[0], -5.283859485344026
        rz q[1], -0.570376061240183
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], 0.8824780130190248
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 5.282765041624873
    skip 1
    ry q[0], -0.2443045281242297
    skip 1
    { # start at cycle 640
        rz q[0], 0.3283166909103361
        ry q[1], 1.761236937555877
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    ry q[1], 0.5873800137085345
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 2.6998378215899304
    skip 1
    ry q[0], -1.7247342963485346
    skip 1
    { # start at cycle 656
        rz q[0], -0.26381094186161214
        rz q[1], -0.6743393488690562
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], 0.9240039111914717
    skip 1
    cnot q[0], q[1]
    skip 1
    ry q[3], 0.7609356290937618
    skip 1
    { # start at cycle 668
        cnot q[2], q[3]
        rz q[0], -4.038049631515634
    }
    skip 1
    ry q[0], -0.5728477883468948
    skip 1
    { # start at cycle 672
        rz q[0], 2.0054675586740482
        rz q[2], -0.33771480700008094
    }
    skip 1
    cnot q[0], q[2]
    skip 3
    rz q[2], -0.8172871208098473
    skip 1
    cnot q[1], q[2]
    skip 3
    rz q[2], 1.5289876768884674
    skip 1
    cnot q[0], q[2]
    skip 3
    rz q[2], -0.022290492295625297
    skip 1
    { # start at cycle 692
        cnot q[1], q[2]
        rz q[0], 1.7291870293308416
    }
    skip 1
    ry q[0], -0.19490567223551328
    skip 1
    { # start at cycle 696
        rz q[0], -2.6209745761763115
        rz q[1], -0.07797873362819521
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], 2.379340899749942
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 1.648775060423092
    skip 1
    ry q[0], -1.3607426075427165
    skip 1
    { # start at cycle 712
        rz q[0], 3.2384153549374
        ry q[1], 1.6784164880562782
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    ry q[1], 0.630769896980843
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 1.0667079641526622
    skip 1
    ry q[0], -1.9306485093225516
    skip 1
    { # start at cycle 728
        rz q[0], -3.9849713540671554
        rz q[1], -0.5593638291803634
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], -1.0761817993598817
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 2.1301601559752603
    skip 1
    ry q[0], -0.9155574302408322
    skip 1
    { # start at cycle 744
        rz q[0], -0.12322160266888504
        ry q[2], 1.400287629533559
    }
    skip 1
    cnot q[0], q[2]
    skip 3
    ry q[2], 0.3045384982266942
    skip 1
    cnot q[1], q[2]
    skip 3
    ry q[2], 0.10725867478096307
    skip 1
    cnot q[0], q[2]
    skip 3
    ry q[2], 0.697159815164998
    skip 1
    { # start at cycle 764
        cnot q[1], q[2]
        rz q[0], 4.27365640046364
    }
    skip 1
    ry q[0], -1.1599484085176397
    skip 1
    { # start at cycle 768
        rz q[0], -0.360610423661718
        rz q[1], -1.1506421559628295
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], 0.9418587472014673
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 2.721438482757726
    skip 1
    ry q[0], -0.6632611677083252
    skip 1
    { # start at cycle 784
        rz q[0], 2.6435209835010203
        ry q[1], 1.9052380817042716
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    ry q[1], 0.3448638082679778
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 0.13366390538250816
    skip 1
    ry q[0], -1.9510113865660934
    skip 1
    { # start at cycle 800
        rz q[0], 0.3796010505064925
        rz q[1], -0.0693623197432713
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], 3.001793969552073
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 1.6401586465381652
    skip 1
    ry q[0], -0.8992122774988253
    skip 1
    { # start at cycle 816
        rz q[0], 2.8860802177133276
        rz q[2], 0.5505442980028787
    }
    skip 1
    cnot q[0], q[2]
    skip 3
    rz q[2], -1.7295513127663147
    skip 1
    cnot q[1], q[2]
    skip 3
    rz q[2], 0.8000246371699489
    skip 1
    cnot q[0], q[2]
    skip 3
    rz q[2], 0.15976817343391914
    skip 1
    { # start at cycle 836
        cnot q[1], q[2]
        rz q[0], 2.1416566118753675
    }
    skip 1
    ry q[0], -2.082380739004034
    skip 1
    { # start at cycle 840
        rz q[0], -1.3700742380023512
        rz q[1], 0.6922885488090474
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], -2.140806363569771
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 4.020100431575642
    skip 1
    ry q[0], -1.3918311027836738
    skip 1
    { # start at cycle 856
        rz q[0], 1.6308704844564539
        ry q[1], 1.453440288966476
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    ry q[1], 0.826438531534907
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], -3.700451798987734
    skip 1
    ry q[0], -0.7316246838916004
    skip 1
    { # start at cycle 872
        rz q[0], 1.9162021681696055
        rz q[1], -1.5020817726663267
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], -1.6250497481302986
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], -0.0687145541285692
    skip 1
    ry q[0], -1.1914978764370574
    skip 1
    { # start at cycle 888
        rz q[0], 2.973163022191176
        rz q[3], 0.8921231046006391
    }
    skip 1
    cnot q[0], q[3]
    skip 3
    rz q[3], 0.7760820196382314
    skip 1
    cnot q[1], q[3]
    skip 3
    rz q[3], 0.536233285762585
    skip 1
    cnot q[0], q[3]
    skip 3
    rz q[3], -0.03245110723428731
    skip 1
    cnot q[2], q[3]
    skip 3
    rz q[3], -0.5936182781709785
    skip 1
    cnot q[0], q[3]
    skip 3
    rz q[3], 0.46196077533276875
    skip 1
    cnot q[1], q[3]
    skip 3
    rz q[3], 0.4555940512220605
    skip 1
    cnot q[0], q[3]
    skip 3
    rz q[0], -0.976206415796816
    skip 1
    ry q[0], -1.24369820707533
    skip 1
    { # start at cycle 934
        rz q[0], 3.031920356934835
        rz q[1], 0.8134035668420858
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], -1.4637439393812561
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], -5.525792547226777
    skip 1
    ry q[0], -1.4747380164378532
    skip 1
    { # start at cycle 950
        rz q[0], -0.7041662385950063
        ry q[1], 1.7805704013591483
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    ry q[1], 0.6629735180565516
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 2.1819901159204353
    skip 1
    ry q[0], -2.774434841924698
    skip 1
    { # start at cycle 966
        rz q[0], 4.009546500260193
        rz q[1], -0.9297141618509214
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], 1.2179270111305658
    skip 1
    cnot q[0], q[1]
    skip 1
    rz q[3], 0.5629074872034168
    skip 1
    { # start at cycle 978
        cnot q[2], q[3]
        rz q[0], -0.6410821649439749
    }
    skip 1
    ry q[0], -0.41782339902666055
    skip 1
    { # start at cycle 982
        rz q[0], -4.641642159727346
        rz q[2], 0.29857089758490885
    }
    skip 1
    cnot q[0], q[2]
    skip 3
    rz q[2], -0.3273954173203454
    skip 1
    cnot q[1], q[2]
    skip 3
    rz q[2], -0.5026899070841165
    skip 1
    cnot q[0], q[2]
    skip 3
    rz q[2], 1.6207254478910937
    skip 1
    { # start at cycle 1002
        cnot q[1], q[2]
        rz q[0], 1.7237305391793658
    }
    skip 1
    ry q[0], -1.4770762075557098
    skip 1
    { # start at cycle 1006
        rz q[0], 0.18768692485376792
        rz q[1], 0.4069828644184137
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], 2.4309151750275704
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], -5.119371844803103
    skip 1
    ry q[0], -1.123990008741451
    skip 1
    { # start at cycle 1022
        rz q[0], -0.8998596974705406
        ry q[1], 1.1928878100787925
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    ry q[1], 0.6113314399386617
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 0.21022747940886966
    skip 1
    ry q[0], -1.9997715028297345
    skip 1
    { # start at cycle 1038
        rz q[0], -4.118472815156759
        rz q[1], 0.2601206748680643
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], 2.4409333782553113
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 1.3106756519268326
    skip 1
    ry q[0], -1.235650681836429
    skip 1
    { # start at cycle 1054
        rz q[0], 4.421683326520447
        ry q[2], 1.5355653228657278
    }
    skip 1
    cnot q[0], q[2]
    skip 3
    ry q[2], 0.2782237368053508
    skip 1
    cnot q[1], q[2]
    skip 3
    ry q[2], -0.034718386809035606
    skip 1
    cnot q[0], q[2]
    skip 3
    ry q[2], 0.9453158874653762
    skip 1
    { # start at cycle 1074
        cnot q[1], q[2]
        rz q[0], 4.075265607107871
    }
    skip 1
    ry q[0], -2.5979173756683713
    skip 1
    { # start at cycle 1078
        rz q[0], -1.1519855761917521
        rz q[1], -0.4730336754476417
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], 0.7926849137050856
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], -1.0977626513472547
    skip 1
    ry q[0], -1.078080214240101
    skip 1
    { # start at cycle 1094
        rz q[0], -1.8558516693863094
        ry q[1], 1.0929937136199657
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    ry q[1], 0.5253269176814371
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], -0.6520097238854814
    skip 1
    ry q[0], -1.981620683429318
    skip 1
    { # start at cycle 1110
        rz q[0], -2.8117396258704135
        rz q[1], -0.7972977834919065
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], 1.8113968362113568
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], -0.7734985433029897
    skip 1
    ry q[0], -0.6202612677040111
    skip 1
    { # start at cycle 1126
        rz q[0], -4.422838931700502
        rz q[2], 0.3771250292340264
    }
    skip 1
    cnot q[0], q[2]
    skip 3
    rz q[2], 0.3089822166296462
    skip 1
    cnot q[1], q[2]
    skip 3
    rz q[2], 0.6307042338150872
    skip 1
    cnot q[0], q[2]
    skip 3
    rz q[2], -1.7330009163075664
    skip 1
    { # start at cycle 1146
        cnot q[1], q[2]
        rz q[0], -0.3471330872391851
    }
    skip 1
    ry q[0], -1.069225237241532
    skip 1
    { # start at cycle 1150
        rz q[0], 0.5952272615239176
        rz q[1], -0.5659698387313854
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], 1.63710760343462
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], -1.004826488063511
    skip 1
    ry q[0], -1.0393143752676466
    skip 1
    { # start at cycle 1166
        rz q[0], 1.3934792469485022
        ry q[1], 1.8392900376854806
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    ry q[1], 0.7026679137297637
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], -0.45993857737732724
    skip 1
    ry q[0], -1.357337843467562
    skip 1
    { # start at cycle 1182
        rz q[0], 4.452773049620155
        rz q[1], -0.3800643567850733
    }
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[1], -1.9396065081405722
    skip 1
    cnot q[0], q[1]
    skip 3
    rz q[0], 1.95086068357997
    skip 1
    ry q[0], -1.4251330621286011
    skip 1
    rz q[0], 3.2685004333072847
    skip 1