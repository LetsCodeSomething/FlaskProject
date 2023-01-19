let dxField,
    dyField,
    cxField,
    cyField,
    scaleField,
    bailoutField,
    nField,
    widthField,
    heightField,
    paletteList,
    formulaList,
    base64Field,
    canvas,
    canvasContext,
    generateButton,
    preset1Button,
    preset2Button,
    preset3Button,
    errorLabel;

let width, height,
    dx, dy,
    cx, cy,
    scale,
    bailout,
    n,
    selectedPalette;

let ufGradPalette = [];
let ufGradPaletteSize;

let bluePalette = [];
let bluePaletteSize;

window.onload =
    function initializeGenerator() {
        dxField = document.getElementById("dx");
        dyField = document.getElementById("dy");
        cxField = document.getElementById("cx");
        cyField = document.getElementById("cy");
        scaleField = document.getElementById("scale");
        bailoutField = document.getElementById("bailout");
        nField = document.getElementById("n");
        widthField = document.getElementById("width");
        heightField = document.getElementById("height");
        paletteList = document.getElementById("palette");
        formulaList = document.getElementById("formula");
        base64Field = document.getElementById("base64");
        canvas = document.getElementById("fracCanvas");

        generateButton = document.getElementById("generateButton");
        generateButton.addEventListener("click", generateFractal);

        preset1Button = document.getElementById("preset1Button");
        preset1Button.addEventListener("click", applyPreset1);
        preset2Button = document.getElementById("preset2Button");
        preset2Button.addEventListener("click", applyPreset2);
        preset3Button = document.getElementById("preset3Button");
        preset3Button.addEventListener("click", applyPreset3);

        errorLabel = document.getElementById("errorLabel");

        ufGradPalette[0]={r:0, g:7, b:100};
        ufGradPalette[1]=({r:8, g:32, b:125});
        ufGradPalette[2]=({r:16, g:57, b:150});
        ufGradPalette[3]=({r:24, g:82, b:175});
        ufGradPalette[4]=({r:32, g:107, b:203});
        ufGradPalette[5]=({r:83, g:144, b:216});
        ufGradPalette[6]=({r:134, g:181, b:229});
        ufGradPalette[7]=({r:185, g:218, b:242});
        ufGradPalette[8]=({r:237, g:255, b:255});
        ufGradPalette[9]=({r:241, g:233, b:189});
        ufGradPalette[10]=({r:245, g:212, b:126});
        ufGradPalette[11]=({r:249, g:191, b:63});
        ufGradPalette[12]=({r:255, g:170, b:0});
        ufGradPalette[13]=({r:189, g:128, b:0});
        ufGradPalette[14]=({r:126, g:86, b:0});
        ufGradPalette[15]=({r:63, g:44, b:0});
        ufGradPalette[16]=({r:0, g:2, b:0});
        ufGradPalette[17]=({r:0, g:3, b:25});
        ufGradPalette[18]=({r:0, g:4, b:50});
        ufGradPalette[19]=({r:0, g:5, b:75});
        ufGradPaletteSize = 20;

        bluePalette[0]={r:37, g:13, b:255};
        bluePalette[1]={r:30, g:10, b:204};
        bluePalette[2]={r:23, g:7, b:153};
        bluePalette[3]={r:16, g:4, b:102};
        bluePalette[4]={r:9, g:2, b:51};
        bluePalette[5]={r:0, g:0, b:0};
        bluePalette[6]={r:9, g:15, b:27};
        bluePalette[7]={r:16, g:30, b:54};
        bluePalette[8]={r:23, g:45, b:81};
        bluePalette[9]={r:30, g:60, b:108};
        bluePalette[10]={r:37, g:75, b:133};
        bluePalette[11]={r:69, g:108, b:156};
        bluePalette[12]={r:101, g:141, b:179};
        bluePalette[13]={r:133, g:174, b:202};
        bluePalette[14]={r:165, g:207, b:225};
        bluePalette[15]={r:194, g:239, b:245};
        bluePalette[16]={r:165, g:193, b:247};
        bluePalette[17]={r:133, g:148, b:249};
        bluePalette[18]={r:101, g:103, b:251};
        bluePalette[19]={r:69, g:58, b:253};
        bluePaletteSize = 20;
    }

function applyPreset1()
{
    formulaList.selectedIndex = 0;
    paletteList.selectedIndex = 1;
    dxField.value = -1.25;
    dyField.value = 0;
    cxField.value = "";
    cyField.value = "";
    scaleField.value = 0.0006;
    bailoutField.value = 256;
    nField.value = 100;
    widthField.value = 900;
    heightField.value = 600;
}

function applyPreset2()
{
    formulaList.selectedIndex = 0;
    paletteList.selectedIndex = 2;
    dxField.value = -1.25;
    dyField.value = -0.41;
    cxField.value = "";
    cyField.value = "";
    scaleField.value = 0.0001;
    bailoutField.value = 256;
    nField.value = 100;
    widthField.value = 900;
    heightField.value = 600;   
}

function applyPreset3()
{
    formulaList.selectedIndex = 1;
    paletteList.selectedIndex = 1;
    dxField.value = 0;
    dyField.value = 0;
    cxField.value = 0.28;
    cyField.value = 0.0113;
    scaleField.value = 0.006;
    bailoutField.value = 256;
    nField.value = 150;
    widthField.value = 900;
    heightField.value = 600;
}

function generateFractal() {
    errorLabel.innerText = "";

    if(!(dxField.value.length > 0 && dyField.value.length > 0 && scaleField.value.length > 0 &&
        bailoutField.value.length > 0 && nField.value.length > 0 &&
        (nField.value.length === parseInt(nField.value).toString().length) &&
        widthField.value.length > 0 &&
        (widthField.value.length === parseInt(widthField.value).toString().length) &&
        heightField.value.length > 0 &&
        (heightField.value.length === parseInt(heightField.value).toString().length)))
    {
        errorLabel.innerText = "Допустимые значения параметров:\nX, Y, CX, CY, Масштаб," +
        "Предел удаления - вещественные числа; Максимум итераций - целое число > 0; " +
        "Ширина - 0 < целое число <= 500; Высота - 0 < целое число <= 250\n";
        return;
    }

    dx = parseFloat(dxField.value);
    dy = parseFloat(dyField.value);
    scale = parseFloat(scaleField.value);
    bailout = parseFloat(bailoutField.value);
    n = parseInt(nField.value);
    width = parseInt(widthField.value);
    height = parseInt(heightField.value);
    selectedPalette = paletteList.selectedIndex;        

    if(!((dx.toString().length === dxField.value.length) && 
         (dy.toString().length === dyField.value.length) && 
         (scale.toString().length === scaleField.value.length) && 
         (bailout.toString().length === bailoutField.value.length) && 
         (n >= 1 && n <= 1000) && 
         (width >= 1 && width <= 500) && (height >= 1 && height <= 250))) 
    {
        errorLabel.innerText = "Допустимые значения параметров:\nX, Y, CX, CY, Масштаб," +
        "Предел удаления - вещественные числа; Максимум итераций - целое число > 0; " +
        "Ширина - 0 < целое число <= 500; Высота - 0 < целое число <= 250\n";
        return;
    }

    if(formulaList.selectedIndex == 1)
    {
        if(cxField.value.length > 0 && 
            (cxField.value.length === parseFloat(cxField.value).toString().length) &&
            cyField.value.length > 0 && 
            (cyField.value.length === parseFloat(cyField.value).toString().length))
        {
            cx = parseFloat(cxField.value);
            cy = parseFloat(cyField.value);
        }
        else
        {
            errorLabel.innerText = "Для этой формулы нужны значения параметров CX, CY.";
            return;
        }
    } 

    canvas.width = width;
    canvas.height = height;
    canvasContext = canvas.getContext("2d");

    if(formulaList.selectedIndex === 0)
    {
        cxField.value = 0;
        cyField.value = 0;
        if(paletteList.selectedIndex === 0)
        {
            drawMandelbrotTwoColors(canvasContext);
        }
        else if(paletteList.selectedIndex === 1)
        {
            drawMandelbrotUfPalette(canvasContext);
        }
        else
        {
            drawMandelbrotBluePalette(canvasContext);
        }
    }
    else
    {
        if(paletteList.selectedIndex === 0)
        {
            drawJuliaTwoColors(canvasContext);
        }
        else if(paletteList.selectedIndex === 1)
        {
            drawJuliaUfPalette(canvasContext);
        }
        else
        {
            
        }
    }

    base64Field.value = canvas.toDataURL();
}

function drawMandelbrotTwoColors(canvasContext)
{
    for(let i = 0; i < width; i++) {
        for(let j = 0; j < height; j++) {
            let cx = (i - width / 2) * scale + dx;
            let cy = (j - height / 2) * scale - dy;
            let tempx1 = 0;
            let tempy1 = 0;
            let tempx2 = 0;
            let tempy2 = 0;
            let iter;

            for(iter = 0; iter < n; iter++)
            {
                tempx2 = (tempx1 * tempx1) - (tempy1 * tempy1) + cx;
                tempy2 = (tempx1 * tempy1 * 2) + cy;

                if (tempx2 * tempx2 + tempy2 * tempy2 > bailout * bailout)
                {
                    break;
                }

                tempx1 = tempx2;
                tempy1 = tempy2;
            }
            if(iter === n)
            {
                canvasContext.fillStyle = "rgba(0,0,0,255)";
                canvasContext.fillRect(i, j, 1, 1);
            }
            else
            {
                canvasContext.fillStyle = "rgba(255,255,255,255)";
                canvasContext.fillRect(i, j, 1, 1);
            }
        }
    }
}

function drawMandelbrotUfPalette(canvasContext)
{
    for(let i = 0; i < width; i++) {
        for(let j = 0; j < height; j++) {
            let cx = (i - width / 2) * scale + dx;
            let cy = (j - height / 2) * scale - dy;
            let tempx1 = 0;
            let tempy1 = 0;
            let tempx2 = 0;
            let tempy2 = 0;
            let iter;

            for(iter = 0; iter < n; iter++) {
                tempx2 = (tempx1 * tempx1) - (tempy1 * tempy1) + cx;
                tempy2 = (tempx1 * tempy1 * 2) + cy;

                if (tempx2 * tempx2 + tempy2 * tempy2 > bailout * bailout) {
                    break;
                }

                tempx1 = tempx2;
                tempy1 = tempy2;
            }

            if(iter === n) {
                canvasContext.fillStyle = "rgba(0,0,0,255)";
                canvasContext.fillRect(i, j, 1, 1);
            }
            else {
                let tempN = iter;

                if(tempN > (ufGradPaletteSize - 1)) {
                    tempN -= Math.trunc(tempN / ufGradPaletteSize) * ufGradPaletteSize;
                }

                let smooth = Math.log2((Math.log(tempx2 * tempx2 + tempy2 * tempy2) / 2) / Math.log(bailout)) * 100;
                smooth = smooth > 100 ? 100 : smooth;

                if (tempN === (ufGradPaletteSize - 1)) {
                    canvasContext.fillStyle = "rgba(" +
                    (ufGradPalette[0].r + smooth * (ufGradPalette[tempN].r - ufGradPalette[0].r) / 100) + "," +
                    (ufGradPalette[0].g + smooth * (ufGradPalette[tempN].g - ufGradPalette[0].g) / 100) + "," +
                    (ufGradPalette[0].b + smooth * (ufGradPalette[tempN].b - ufGradPalette[0].b) / 100) + ",255)";

                    canvasContext.fillRect(i, j, 1, 1);
                }
                else {
                    canvasContext.fillStyle = "rgba(" +
                        (ufGradPalette[tempN + 1].r + smooth * (ufGradPalette[tempN].r - ufGradPalette[tempN + 1].r) / 100) + "," +
                        (ufGradPalette[tempN + 1].g + smooth * (ufGradPalette[tempN].g - ufGradPalette[tempN + 1].g) / 100) + "," +
                        (ufGradPalette[tempN + 1].b + smooth * (ufGradPalette[tempN].b - ufGradPalette[tempN + 1].b) / 100) + ",255)";

                    canvasContext.fillRect(i, j, 1, 1);
                }
            }
        }
    }
}

function drawMandelbrotBluePalette(canvasContext)
{
    for(let i = 0; i < width; i++) {
        for(let j = 0; j < height; j++) {
            let cx = (i - width / 2) * scale + dx;
            let cy = (j - height / 2) * scale - dy;
            let tempx1 = 0;
            let tempy1 = 0;
            let tempx2 = 0;
            let tempy2 = 0;
            let iter;

            for(iter = 0; iter < n; iter++) {
                tempx2 = (tempx1 * tempx1) - (tempy1 * tempy1) + cx;
                tempy2 = (tempx1 * tempy1 * 2) + cy;

                if (tempx2 * tempx2 + tempy2 * tempy2 > bailout * bailout) {
                    break;
                }

                tempx1 = tempx2;
                tempy1 = tempy2;
            }

            if(iter === n) {
                canvasContext.fillStyle = "rgba(0,0,0,255)";
                canvasContext.fillRect(i, j, 1, 1);
            }
            else {
                let tempN = iter;

                if(tempN > (bluePaletteSize - 1)) {
                    tempN -= Math.trunc(tempN / bluePaletteSize) * bluePaletteSize;
                }

                let smooth = Math.log2((Math.log(tempx2 * tempx2 + tempy2 * tempy2) / 2) / Math.log(bailout)) * 100;
                smooth = smooth > 100 ? 100 : smooth;

                if (tempN === (bluePaletteSize - 1)) {
                    canvasContext.fillStyle = "rgba(" +
                    (bluePalette[0].r + smooth * (bluePalette[tempN].r - bluePalette[0].r) / 100) + "," +
                    (bluePalette[0].g + smooth * (bluePalette[tempN].g - bluePalette[0].g) / 100) + "," +
                    (bluePalette[0].b + smooth * (bluePalette[tempN].b - bluePalette[0].b) / 100) + ",255)";

                    canvasContext.fillRect(i, j, 1, 1);
                }
                else {
                    canvasContext.fillStyle = "rgba(" +
                        (bluePalette[tempN + 1].r + smooth * (bluePalette[tempN].r - bluePalette[tempN + 1].r) / 100) + "," +
                        (bluePalette[tempN + 1].g + smooth * (bluePalette[tempN].g - bluePalette[tempN + 1].g) / 100) + "," +
                        (bluePalette[tempN + 1].b + smooth * (bluePalette[tempN].b - bluePalette[tempN + 1].b) / 100) + ",255)";

                    canvasContext.fillRect(i, j, 1, 1);
                }
            }
        }
    }
}

function drawJuliaTwoColors(canvasContext)
{
    for(let i = 0; i < width; i++) {
        for(let j = 0; j < height; j++) {
            let tempx1 = (i - width / 2) * scale + dx;
            let tempy1 = (j - height / 2) * scale + dy;
            let tempx2 = 0;
            let tempy2 = 0;
            let iter;

            for(iter = 0; iter < n; iter++)
            {
                tempx2 = (tempx1 * tempx1) - (tempy1 * tempy1) + cx;
                tempy2 = (tempx1 * tempy1 * 2) - cy;

                if (tempx2 * tempx2 + tempy2 * tempy2 > bailout * bailout)
                {
                    break;
                }

                tempx1 = tempx2;
                tempy1 = tempy2;
            }
            if(iter === n)
            {
                canvasContext.fillStyle = "rgba(0,0,0,255)";
                canvasContext.fillRect(i, j, 1, 1);
            }
            else
            {
                canvasContext.fillStyle = "rgba(255,255,255,255)";
                canvasContext.fillRect(i, j, 1, 1);
            }
        }
    }
}

function drawJuliaUfPalette(canvasContext)
{
    for(let i = 0; i < width; i++) {
        for(let j = 0; j < height; j++) {
            let tempx1 = (i - width / 2) * scale + dx;
            let tempy1 = (j - height / 2) * scale + dy;
            let tempx2 = 0;
            let tempy2 = 0;
            let iter;

            for(iter = 0; iter < n; iter++) {
                tempx2 = (tempx1 * tempx1) - (tempy1 * tempy1) + cx;
                tempy2 = (tempx1 * tempy1 * 2) - cy;

                if (tempx2 * tempx2 + tempy2 * tempy2 > bailout * bailout) {
                    break;
                }

                tempx1 = tempx2;
                tempy1 = tempy2;
            }

            if(iter === n) {
                canvasContext.fillStyle = "rgba(0,0,0,255)";
                canvasContext.fillRect(i, j, 1, 1);
            }
            else {
                let tempN = iter;

                if(tempN > (ufGradPaletteSize - 1)) {
                    tempN -= Math.trunc(tempN / ufGradPaletteSize) * ufGradPaletteSize;
                }

                let smooth = Math.log2((Math.log(tempx2 * tempx2 + tempy2 * tempy2) / 2) / Math.log(bailout)) * 100;
                smooth = smooth > 100 ? 100 : smooth;

                if (tempN === (ufGradPaletteSize - 1)) {
                    canvasContext.fillStyle = "rgba(" +
                    (ufGradPalette[0].r + smooth * (ufGradPalette[tempN].r - ufGradPalette[0].r) / 100) + "," +
                    (ufGradPalette[0].g + smooth * (ufGradPalette[tempN].g - ufGradPalette[0].g) / 100) + "," +
                    (ufGradPalette[0].b + smooth * (ufGradPalette[tempN].b - ufGradPalette[0].b) / 100) + ",255)";

                    canvasContext.fillRect(i, j, 1, 1);
                }
                else {
                    canvasContext.fillStyle = "rgba(" +
                        (ufGradPalette[tempN + 1].r + smooth * (ufGradPalette[tempN].r - ufGradPalette[tempN + 1].r) / 100) + "," +
                        (ufGradPalette[tempN + 1].g + smooth * (ufGradPalette[tempN].g - ufGradPalette[tempN + 1].g) / 100) + "," +
                        (ufGradPalette[tempN + 1].b + smooth * (ufGradPalette[tempN].b - ufGradPalette[tempN + 1].b) / 100) + ",255)";

                    canvasContext.fillRect(i, j, 1, 1);
                }
            }
        }
    }
}