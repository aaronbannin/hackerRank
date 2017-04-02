//: Playground - noun: a place where people can play

import Cocoa

var str = "Hello, playground"

//var inputValues = [[Int]]()




class hourGlassSum {
    
    var inputValues:[[Int]]
    var baseWidth: Int
    var hourGlassSums = [(x: Int, y: Int, value: Int)]()
    
    init(inputValues: [[Int]], baseWidth: Int) {
        self.inputValues = inputValues
        self.baseWidth = baseWidth
    }
    
    func main() {

        for yvalue in 0...inputValues.count - baseWidth - 1 {
            for xvalue in 0...inputValues[yvalue].count - baseWidth - 1 {
                let top = inputValues[yvalue][xvalue...xvalue + 2].reduce(0, combine: +)
                let middle = inputValues[yvalue + 1][xvalue + 1]
                let bottom = inputValues[yvalue + 2][xvalue...xvalue + 2].reduce(0, combine: +)
                let sum = top + middle + bottom
                
                hourGlassSums.append((x: xvalue, y: yvalue, value: sum))
                
            }
        }
        
        hourGlassSums.sortInPlace { $0.value > $1.value }
        
    }
    
    class func formatToArray(input: String) -> [Int] {
        let array = input.characters.split(" ").map(String.init)
        return array.map { Int($0)! }
    }
    
}

var inputValues = [hourGlassSum.formatToArray(readLine()!)]
inputValues.append(hourGlassSum.formatToArray(readLine()!))
inputValues.append(hourGlassSum.formatToArray(readLine()!))
inputValues.append(hourGlassSum.formatToArray(readLine()!))
inputValues.append(hourGlassSum.formatToArray(readLine()!))
inputValues.append(hourGlassSum.formatToArray(readLine()!))

let new = hourGlassSum.init(inputValues: inputValues, baseWidth: 2)
new.main()
print(new.hourGlassSums[0].value)





