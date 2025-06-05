INSERT INTO song (name, artist, file_location) VALUES ('Candy', 'MSTR K', 'candy.wav');

-- Get the song id for 'Candy' by MSTR K
WITH song_id_cte AS (
    SELECT id AS song_id FROM song WHERE name = 'Candy' AND artist = 'MSTR K' LIMIT 1
)

-- Insert multiple timing entries for the song using the retrieved song_id
INSERT INTO timing (song_id, key_id, time_point)
SELECT song_id, 0, 0.900 FROM song_id_cte
UNION ALL
SELECT song_id, 2, 1.316 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 1.759 FROM song_id_cte
UNION ALL
SELECT song_id, 2, 2.202 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 2.654 FROM song_id_cte
UNION ALL
SELECT song_id, 3, 3.092 FROM song_id_cte
UNION ALL
SELECT song_id, 5, 3.362 FROM song_id_cte
UNION ALL
SELECT song_id, 6, 3.566 FROM song_id_cte
UNION ALL
SELECT song_id, 8, 3.758 FROM song_id_cte
UNION ALL
SELECT song_id, 7, 4.013 FROM song_id_cte
UNION ALL

SELECT song_id, 0, 4.451 FROM song_id_cte
UNION ALL
SELECT song_id, 2, 4.867 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 5.310 FROM song_id_cte
UNION ALL
SELECT song_id, 2, 5.753 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 6.205 FROM song_id_cte
UNION ALL
SELECT song_id, 3, 6.643 FROM song_id_cte
UNION ALL
SELECT song_id, 5, 6.913 FROM song_id_cte
UNION ALL
SELECT song_id, 6, 7.117 FROM song_id_cte
UNION ALL
SELECT song_id, 8, 7.309 FROM song_id_cte
UNION ALL
SELECT song_id, 7, 7.564 FROM song_id_cte
UNION ALL

SELECT song_id, 0, 7.852 FROM song_id_cte
UNION ALL
SELECT song_id, 2, 8.268 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 8.711 FROM song_id_cte
UNION ALL
SELECT song_id, 2, 9.158 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 9.606 FROM song_id_cte
UNION ALL
SELECT song_id, 3, 10.044 FROM song_id_cte
UNION ALL
SELECT song_id, 5, 10.314 FROM song_id_cte
UNION ALL
SELECT song_id, 6, 10.518 FROM song_id_cte
UNION ALL
SELECT song_id, 8, 10.710 FROM song_id_cte
UNION ALL
SELECT song_id, 7, 10.965 FROM song_id_cte
UNION ALL

SELECT song_id, 0, 11.370 FROM song_id_cte
UNION ALL
SELECT song_id, 2, 11.786 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 12.221 FROM song_id_cte
UNION ALL
SELECT song_id, 2, 12.682 FROM song_id_cte
UNION ALL

SELECT song_id, 3, 13.201 FROM song_id_cte
UNION ALL
SELECT song_id, 5, 13.481 FROM song_id_cte
UNION ALL
SELECT song_id, 3, 14.045 FROM song_id_cte
UNION ALL
SELECT song_id, 5, 14.225 FROM song_id_cte
UNION ALL
SELECT song_id, 3, 14.521 FROM song_id_cte
UNION ALL
SELECT song_id, 5, 14.686 FROM song_id_cte
UNION ALL

SELECT song_id, 0, 14.893 FROM song_id_cte
UNION ALL
SELECT song_id, 2, 15.309 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 15.832 FROM song_id_cte
UNION ALL
SELECT song_id, 2, 16.285 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 16.737 FROM song_id_cte
UNION ALL
SELECT song_id, 3, 17.175 FROM song_id_cte
UNION ALL
SELECT song_id, 5, 17.445 FROM song_id_cte
UNION ALL
SELECT song_id, 6, 17.649 FROM song_id_cte
UNION ALL
SELECT song_id, 8, 17.841 FROM song_id_cte
UNION ALL
SELECT song_id, 7, 18.096 FROM song_id_cte
UNION ALL

SELECT song_id, 0, 18.420 FROM song_id_cte
UNION ALL
SELECT song_id, 2, 18.836 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 19.279 FROM song_id_cte
UNION ALL
SELECT song_id, 2, 19.732 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 20.184 FROM song_id_cte
UNION ALL
SELECT song_id, 3, 20.622 FROM song_id_cte
UNION ALL
SELECT song_id, 5, 20.892 FROM song_id_cte
UNION ALL
SELECT song_id, 6, 21.096 FROM song_id_cte
UNION ALL
SELECT song_id, 8, 21.288 FROM song_id_cte
UNION ALL
SELECT song_id, 7, 21.543 FROM song_id_cte
UNION ALL

SELECT song_id, 0, 40.915963719 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 41.373061224 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 41.819863946 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 42.264172336 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 42.692176871 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 42.908775510 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 43.160589569 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 43.579002268 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 43.791405896 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 44.036553288 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 44.470068027 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 44.686621315 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 44.923650794 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 45.371451247 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 45.598299320 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 45.847596372 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 46.266281179 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 46.714603175 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 47.188208617 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 47.619546485 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 48.043514739 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 48.503968254 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 48.948934240 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 49.391746032 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 49.814920635 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 50.017120181 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 50.269773243 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 50.731927438 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 50.938140590 FROM song_id_cte
UNION ALL
SELECT song_id, 4, 51.149863946 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 51.579297052 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 52.040702948 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 52.502857143 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 52.937074830 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 53.404603175 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 53.827709751 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 54.260793651 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 54.718049887 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 55.162970522 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 55.389410431 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 55.611156463 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 56.039229025 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 56.262176871 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 56.460453515 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 56.930929705 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 57.387460317 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 57.845532880 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 58.279070295 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 60.464081633 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 60.950725624 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 61.398798186 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 61.837052154 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 64.028594104 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 64.499863946 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 64.943922902 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 65.379229025 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 67.612766440 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 68.066235828 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 68.503696145 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 68.946666667 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 71.139954649 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 71.585011338 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 72.077278912 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 72.475328798 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 72.932154195 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 73.371678005 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 73.818480726 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 74.271746032 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 74.705759637 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 75.157981859 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 75.611655329 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 76.053424036 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 76.482335601 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 76.742063492 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 77.171043084 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 77.392040816 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 77.826666667 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 78.294353741 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 78.750498866 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 79.194625850 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 79.646122449 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 80.080702948 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 80.499705215 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 81.159954649 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 81.384965986 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 81.613151927 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 81.839342404 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 82.273492063 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 82.718934240 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 83.162993197 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 83.608253968 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 84.512154195 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 85.398662132 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 85.854965986 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 86.277233560 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 86.731564626 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 87.196507937 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 88.061405896 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 88.922312925 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 89.384988662 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 89.845532880 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 90.290589569 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 90.728253968 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 91.628049887 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 92.481201814 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 92.923446712 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 93.357460317 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 93.806099773 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 94.268049887 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 95.169024943 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 96.026984127 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 96.484285714 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 96.936870748 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 97.404761905 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 97.850544218 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 98.742154195 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 99.639614512 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 100.049319728 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 100.491655329 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 100.920022676 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 101.382653061 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 102.272448980 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 103.145328798 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 103.595600907 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 104.476848073 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 104.926371882 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 105.821904762 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 106.713582766 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 107.171292517 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 108.061950113 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 108.465170068 FROM song_id_cte
UNION ALL
SELECT song_id, 1, 109.390136054 FROM song_id_cte
UNION ALL
SELECT song_id, 2, 110.265419501 FROM song_id_cte
UNION ALL
SELECT song_id, 3, 110.733378685 FROM song_id_cte
UNION ALL
SELECT song_id, 4, 111.180702948 FROM song_id_cte
UNION ALL
SELECT song_id, 5, 111.590997732 FROM song_id_cte
UNION ALL
SELECT song_id, 6, 112.053537415 FROM song_id_cte
UNION ALL
SELECT song_id, 7, 112.505306122 FROM song_id_cte
UNION ALL
SELECT song_id, 8, 113.001655329 FROM song_id_cte
UNION ALL
SELECT song_id, 0, 113.440249433 FROM song_id_cte;
