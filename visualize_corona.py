from scipy.integrate import odeint
import matplotlib.pyplot as plt

# for our simulation, let TRANSMISSION_RATE = 0.04 meaning 4% chance to transmit the virus if you have it
# and RECOVERY_RATE = 1/14 meaning that you can transmit the virus for the next 14 days


TRANSMISSION_RATE = 0.04
RECOVERY_RATE = 1 / 14


class SimVirus():

    # initialize with default 1000 population, 1 infected, 0 removed, time period of
    # 160 days and contact rate of 5 people per day
    def __init__(self, population=1000, inf=1, rem=0, days=160, contact_rate=5):
        self.population = population
        self.inf = inf
        self.rem = rem
        # susceptible is the population that has not yet gotten the virus
        self.susc = self.population - self.inf - self.rem
        self.days = range(0, days)

        # effective contact rate is the product of the TRANSMISSION_RATE and the contact rate
        self.effective_contact_rate = contact_rate * TRANSMISSION_RATE

        # state of our population
        self.state = [self.susc, self.inf, self.rem]

        ret = odeint(self.deriv, self.state, self.days)
        S, I, R = ret.T


        fig = plt.figure(facecolor='w')
        ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
        ax.plot(self.days, S, 'b', alpha=0.5, lw=2, label='Susceptible')
        ax.plot(self.days, I , 'r', alpha=0.5, lw=2, label='Infected')
        ax.plot(self.days, R , 'g', alpha=0.5, lw=2, label='Removed')
        ax.set_xlabel('Days')
        ax.set_ylabel('Population')
        ax.yaxis.set_tick_params(length=0)
        ax.xaxis.set_tick_params(length=0)
        ax.grid(b=True, which='major', c='w', lw=2, ls='-')
        legend = ax.legend()
        legend.get_frame().set_alpha(0.5)
        for spine in ('top', 'right', 'bottom', 'left'):
            ax.spines[spine].set_visible(False)
        plt.show()



    def deriv(self, y0, t):
        s, i, r = y0
        # Change in S population over time
        dsdt = -self.effective_contact_rate * s * i / self.population
        # Change in I population over time
        didt = self.effective_contact_rate * s * i / self.population - RECOVERY_RATE * i
        # Change in R population over time
        drdt = RECOVERY_RATE * i
        return dsdt, didt, drdt


