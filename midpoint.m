myFolder = './train_grayscale';
filePattern = fullfile(myFolder, '*.jpg');
jpegFiles = dir(filePattern);
length(jpegFiles)
for k = 1:length(jpegFiles)
    baseFileName = jpegFiles(k).name;
    fullFileName = fullfile(myFolder, baseFileName);
    fprintf(1, 'Now reading %s\n', fullFileName);
    img = imread(fullFileName);
    B1 = padarray(img,[1,1]);
    [r,c] = size(B1);
    for i =2:r-1
        for j = 2:c-1
            out = [B1(i-1,j-1),B1(i-1,j),B1(i-1,j+1),...
                B1(i,j-1),B1(i,j),B1(i,j+1),...
                B1(i+1,j-1),B1(i+1,j),B1(i+1,j+1)];
            a = max(out);
            b = min(out);
            OUT(i,j) = (a+b)/2;
        end
    end
    fullFileName = fullfile('./train_midpoint', baseFileName);
    imwrite(OUT, fullFileName);
end