import math


def main():
    A, B, H, M = map(int, input().split())
    PI = math.pi

    # Hour
    h_deg = 360 - 360 * (H + M / 60) / 12 + 90.0
    h_rad = h_deg * PI / 180.0
    # print(h_deg)
    h_x, h_y = A * math.cos(h_rad), A * math.sin(h_rad)
    # print(h_x, h_y)

    # Minute
    m_deg = 360 - 360 * (M / 60) + 90.0
    m_rad = m_deg * PI / 180.0
    # print(m_deg)
    m_x, m_y = B * math.cos(m_rad), B * math.sin(m_rad)
    # print(m_x, m_y)

    print(math.sqrt((h_x - m_x)**2 + (h_y - m_y)**2))


main()
