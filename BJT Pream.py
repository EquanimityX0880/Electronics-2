# BJT Class A Preamp
# Setup: State specs.
Vcc = 9
R3 = 10000
Gain = [8, 9, 10]
Blow = 20
Bhigh = 20000
Beta = 100

def a():
    i = 0
    while(len(Gain) > i):
        print(len(Gain))
        R4 = R3 / Gain[i]
        Rout = R4*10
        # Step 1: Determine ICSaturation, assuming the BJT is shorted
        ICSaturation = Vcc / (R3 + R4)
        Iq = ICSaturation/2
        # Determine Vceq
        Vceq = Vcc - Iq*(R3+R4)
        # Determine Ve and Vb
        Ve = Iq*R4
        Vb = Ve + 0.65

        #Find R2
        R2 = (Beta*R4)/10
        R1 = Vcc*(R2/Vb)-R2
        ParallelR1R2 = (R1*R2)/(R1+R2)

        # AC Coupling Capacitors must be at least this value
        C1 = 1/(2*3.141*ParallelR1R2*20)
        C2 = 1/(2*3.141*ParallelR1R2*10*20)

        print("Required Values")
        print("R1: " , R1,
        "\nR2: " , R2,
        "\nR3: " , R3,
        "\nR4: " , R4,
        "\nRout: " , Rout,
        "\nC1: " , C1,
        "\nC2: " , C2
        )
        print(" ")
        i +=1

a()
