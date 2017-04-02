import Foundation

class meal {
    
    var cost:Double
    var tipPercent: Double
    var taxPercent: Double
    
    init(cost: Double, tipPercent: Double, taxPercent: Double) {
        self.cost = cost
        self.tipPercent = tipPercent
        self.taxPercent = taxPercent
    }
    
    func totalCost() -> String {
        let calculatedCost = round(cost + (cost *  tipPercent) + (cost * taxPercent))
        return "The total meal cost is \(calculatedCost) dollars."
    }
    
    class func main(stdin: [String]) -> String {
        let formattedInput = stdin.map { Double($0)! }
        let newMeal = meal(cost: formattedInput[0], tipPercent: formattedInput[1], taxPercent: formattedInput[2])
        return newMeal.totalCost()
    }
    
}

var input = [String]()
input.append(readLine()!)
input.append(readLine()!)
input.append(readLine()!)
meal.main(input)