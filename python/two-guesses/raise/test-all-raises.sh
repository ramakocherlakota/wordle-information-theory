echo -----
python guess.py raise=-----  | jq .expected_uncertainty_after_guess
echo ----B
python guess.py raise=----B  | jq .expected_uncertainty_after_guess
echo ----W
python guess.py raise=----W  | jq .expected_uncertainty_after_guess
echo ---B-
python guess.py raise=---B-  | jq .expected_uncertainty_after_guess
echo ---BB
python guess.py raise=---BB  | jq .expected_uncertainty_after_guess
echo ---BW
python guess.py raise=---BW  | jq .expected_uncertainty_after_guess
echo ---W-
python guess.py raise=---W-  | jq .expected_uncertainty_after_guess
echo ---WB
python guess.py raise=---WB  | jq .expected_uncertainty_after_guess
echo ---WW
python guess.py raise=---WW  | jq .expected_uncertainty_after_guess
echo --B--
python guess.py raise=--B--  | jq .expected_uncertainty_after_guess
echo --B-B
python guess.py raise=--B-B  | jq .expected_uncertainty_after_guess
echo --B-W
python guess.py raise=--B-W  | jq .expected_uncertainty_after_guess
echo --BB-
python guess.py raise=--BB-  | jq .expected_uncertainty_after_guess
echo --BBB
python guess.py raise=--BBB  | jq .expected_uncertainty_after_guess
echo --BBW
python guess.py raise=--BBW  | jq .expected_uncertainty_after_guess
echo --BW-
python guess.py raise=--BW-  | jq .expected_uncertainty_after_guess
echo --BWB
python guess.py raise=--BWB  | jq .expected_uncertainty_after_guess
echo --BWW
python guess.py raise=--BWW  | jq .expected_uncertainty_after_guess
echo --W--
python guess.py raise=--W--  | jq .expected_uncertainty_after_guess
echo --W-B
python guess.py raise=--W-B  | jq .expected_uncertainty_after_guess
echo --W-W
python guess.py raise=--W-W  | jq .expected_uncertainty_after_guess
echo --WB-
python guess.py raise=--WB-  | jq .expected_uncertainty_after_guess
echo --WW-
python guess.py raise=--WW-  | jq .expected_uncertainty_after_guess
echo --WWB
python guess.py raise=--WWB  | jq .expected_uncertainty_after_guess
echo --WWW
python guess.py raise=--WWW  | jq .expected_uncertainty_after_guess
echo -B---
python guess.py raise=-B---  | jq .expected_uncertainty_after_guess
echo -B--B
python guess.py raise=-B--B  | jq .expected_uncertainty_after_guess
echo -B--W
python guess.py raise=-B--W  | jq .expected_uncertainty_after_guess
echo -B-B-
python guess.py raise=-B-B-  | jq .expected_uncertainty_after_guess
echo -B-BB
python guess.py raise=-B-BB  | jq .expected_uncertainty_after_guess
echo -B-W-
python guess.py raise=-B-W-  | jq .expected_uncertainty_after_guess
echo -B-WB
python guess.py raise=-B-WB  | jq .expected_uncertainty_after_guess
echo -B-WW
python guess.py raise=-B-WW  | jq .expected_uncertainty_after_guess
echo -BB--
python guess.py raise=-BB--  | jq .expected_uncertainty_after_guess
echo -BB-B
python guess.py raise=-BB-B  | jq .expected_uncertainty_after_guess
echo -BBB-
python guess.py raise=-BBB-  | jq .expected_uncertainty_after_guess
echo -BBW-
python guess.py raise=-BBW-  | jq .expected_uncertainty_after_guess
echo -BW--
python guess.py raise=-BW--  | jq .expected_uncertainty_after_guess
echo -BWW-
python guess.py raise=-BWW-  | jq .expected_uncertainty_after_guess
echo -W---
python guess.py raise=-W---  | jq .expected_uncertainty_after_guess
echo -W--B
python guess.py raise=-W--B  | jq .expected_uncertainty_after_guess
echo -W--W
python guess.py raise=-W--W  | jq .expected_uncertainty_after_guess
echo -W-B-
python guess.py raise=-W-B-  | jq .expected_uncertainty_after_guess
echo -W-BB
python guess.py raise=-W-BB  | jq .expected_uncertainty_after_guess
echo -W-BW
python guess.py raise=-W-BW  | jq .expected_uncertainty_after_guess
echo -W-W-
python guess.py raise=-W-W-  | jq .expected_uncertainty_after_guess
echo -W-WB
python guess.py raise=-W-WB  | jq .expected_uncertainty_after_guess
echo -W-WW
python guess.py raise=-W-WW  | jq .expected_uncertainty_after_guess
echo -WB--
python guess.py raise=-WB--  | jq .expected_uncertainty_after_guess
echo -WB-B
python guess.py raise=-WB-B  | jq .expected_uncertainty_after_guess
echo -WB-W
python guess.py raise=-WB-W  | jq .expected_uncertainty_after_guess
echo -WBB-
python guess.py raise=-WBB-  | jq .expected_uncertainty_after_guess
echo -WBWB
python guess.py raise=-WBWB  | jq .expected_uncertainty_after_guess
echo -WW--
python guess.py raise=-WW--  | jq .expected_uncertainty_after_guess
echo -WW-B
python guess.py raise=-WW-B  | jq .expected_uncertainty_after_guess
echo -WW-W
python guess.py raise=-WW-W  | jq .expected_uncertainty_after_guess
echo -WWB-
python guess.py raise=-WWB-  | jq .expected_uncertainty_after_guess
echo -WWW-
python guess.py raise=-WWW-  | jq .expected_uncertainty_after_guess
echo -WWWB
python guess.py raise=-WWWB  | jq .expected_uncertainty_after_guess
echo -WWWW
python guess.py raise=-WWWW  | jq .expected_uncertainty_after_guess
echo B----
python guess.py raise=B----  | jq .expected_uncertainty_after_guess
echo B---B
python guess.py raise=B---B  | jq .expected_uncertainty_after_guess
echo B---W
python guess.py raise=B---W  | jq .expected_uncertainty_after_guess
echo B--B-
python guess.py raise=B--B-  | jq .expected_uncertainty_after_guess
echo B--BB
python guess.py raise=B--BB  | jq .expected_uncertainty_after_guess
echo B--W-
python guess.py raise=B--W-  | jq .expected_uncertainty_after_guess
echo B--WW
python guess.py raise=B--WW  | jq .expected_uncertainty_after_guess
echo B-B--
python guess.py raise=B-B--  | jq .expected_uncertainty_after_guess
echo B-B-W
python guess.py raise=B-B-W  | jq .expected_uncertainty_after_guess
echo B-W--
python guess.py raise=B-W--  | jq .expected_uncertainty_after_guess
echo B-W-B
python guess.py raise=B-W-B  | jq .expected_uncertainty_after_guess
echo B-W-W
python guess.py raise=B-W-W  | jq .expected_uncertainty_after_guess
echo B-WBB
python guess.py raise=B-WBB  | jq .expected_uncertainty_after_guess
echo B-WW-
python guess.py raise=B-WW-  | jq .expected_uncertainty_after_guess
echo B-WWW
python guess.py raise=B-WWW  | jq .expected_uncertainty_after_guess
echo BB---
python guess.py raise=BB---  | jq .expected_uncertainty_after_guess
echo BB--B
python guess.py raise=BB--B  | jq .expected_uncertainty_after_guess
echo BB--W
python guess.py raise=BB--W  | jq .expected_uncertainty_after_guess
echo BB-W-
python guess.py raise=BB-W-  | jq .expected_uncertainty_after_guess
echo BBB--
python guess.py raise=BBB--  | jq .expected_uncertainty_after_guess
echo BBBBB
python guess.py raise=BBBBB  | jq .expected_uncertainty_after_guess
echo BBW--
python guess.py raise=BBW--  | jq .expected_uncertainty_after_guess
echo BW---
python guess.py raise=BW---  | jq .expected_uncertainty_after_guess
echo BW--W
python guess.py raise=BW--W  | jq .expected_uncertainty_after_guess
echo BW-B-
python guess.py raise=BW-B-  | jq .expected_uncertainty_after_guess
echo BWW--
python guess.py raise=BWW--  | jq .expected_uncertainty_after_guess
echo W----
python guess.py raise=W----  | jq .expected_uncertainty_after_guess
echo W---B
python guess.py raise=W---B  | jq .expected_uncertainty_after_guess
echo W---W
python guess.py raise=W---W  | jq .expected_uncertainty_after_guess
echo W--B-
python guess.py raise=W--B-  | jq .expected_uncertainty_after_guess
echo W--BB
python guess.py raise=W--BB  | jq .expected_uncertainty_after_guess
echo W--BW
python guess.py raise=W--BW  | jq .expected_uncertainty_after_guess
echo W--W-
python guess.py raise=W--W-  | jq .expected_uncertainty_after_guess
echo W--WB
python guess.py raise=W--WB  | jq .expected_uncertainty_after_guess
echo W--WW
python guess.py raise=W--WW  | jq .expected_uncertainty_after_guess
echo W-B--
python guess.py raise=W-B--  | jq .expected_uncertainty_after_guess
echo W-B-B
python guess.py raise=W-B-B  | jq .expected_uncertainty_after_guess
echo W-B-W
python guess.py raise=W-B-W  | jq .expected_uncertainty_after_guess
echo W-BB-
python guess.py raise=W-BB-  | jq .expected_uncertainty_after_guess
echo W-BW-
python guess.py raise=W-BW-  | jq .expected_uncertainty_after_guess
echo W-BWB
python guess.py raise=W-BWB  | jq .expected_uncertainty_after_guess
echo W-BWW
python guess.py raise=W-BWW  | jq .expected_uncertainty_after_guess
echo W-W--
python guess.py raise=W-W--  | jq .expected_uncertainty_after_guess
echo W-W-B
python guess.py raise=W-W-B  | jq .expected_uncertainty_after_guess
echo W-W-W
python guess.py raise=W-W-W  | jq .expected_uncertainty_after_guess
echo W-WB-
python guess.py raise=W-WB-  | jq .expected_uncertainty_after_guess
echo W-WW-
python guess.py raise=W-WW-  | jq .expected_uncertainty_after_guess
echo W-WWW
python guess.py raise=W-WWW  | jq .expected_uncertainty_after_guess
echo WB---
python guess.py raise=WB---  | jq .expected_uncertainty_after_guess
echo WB--B
python guess.py raise=WB--B  | jq .expected_uncertainty_after_guess
echo WB--W
python guess.py raise=WB--W  | jq .expected_uncertainty_after_guess
echo WB-B-
python guess.py raise=WB-B-  | jq .expected_uncertainty_after_guess
echo WB-BB
python guess.py raise=WB-BB  | jq .expected_uncertainty_after_guess
echo WB-W-
python guess.py raise=WB-W-  | jq .expected_uncertainty_after_guess
echo WB-WW
python guess.py raise=WB-WW  | jq .expected_uncertainty_after_guess
echo WBB--
python guess.py raise=WBB--  | jq .expected_uncertainty_after_guess
echo WBW--
python guess.py raise=WBW--  | jq .expected_uncertainty_after_guess
echo WW---
python guess.py raise=WW---  | jq .expected_uncertainty_after_guess
echo WW--B
python guess.py raise=WW--B  | jq .expected_uncertainty_after_guess
echo WW--W
python guess.py raise=WW--W  | jq .expected_uncertainty_after_guess
echo WW-B-
python guess.py raise=WW-B-  | jq .expected_uncertainty_after_guess
echo WW-BB
python guess.py raise=WW-BB  | jq .expected_uncertainty_after_guess
echo WW-W-
python guess.py raise=WW-W-  | jq .expected_uncertainty_after_guess
echo WW-WB
python guess.py raise=WW-WB  | jq .expected_uncertainty_after_guess
echo WW-WW
python guess.py raise=WW-WW  | jq .expected_uncertainty_after_guess
echo WWB--
python guess.py raise=WWB--  | jq .expected_uncertainty_after_guess
echo WWB-B
python guess.py raise=WWB-B  | jq .expected_uncertainty_after_guess
echo WWBBB
python guess.py raise=WWBBB  | jq .expected_uncertainty_after_guess
echo WWW--
python guess.py raise=WWW--  | jq .expected_uncertainty_after_guess
echo WWW-B
python guess.py raise=WWW-B  | jq .expected_uncertainty_after_guess
echo WWW-W
python guess.py raise=WWW-W  | jq .expected_uncertainty_after_guess
echo WWWW-
python guess.py raise=WWWW-  | jq .expected_uncertainty_after_guess
