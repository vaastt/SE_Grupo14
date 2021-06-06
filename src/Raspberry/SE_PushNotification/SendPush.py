import FCMManager as fcm

tokens = ["cZO8o2tVQb2zKC-s6SkA-7:APA91bFESs1bKXS83W0knZITfq82gDNENk23LOJLF0PXhsdnknTBZHhJzUVYbjyOrtKd18eY96Wrg24Da2dYsjrB2kepoUb6pqSo4_Qs0VVKcc12mulfc6Obg_GQfKbkkN6iedRr66Li"]

fcm.sendPush("Camera na Campainha", "O sensor detectou movimento", tokens)