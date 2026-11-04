
"""
DREAMNOVA AI backend starter.
Run locally with: python server.py
Install dependencies: pip install -r requirements.txt

Keep OPENAI_API_KEY in an environment variable.
Never put your secret API key in index.html.
"""

import os
from flask import Flask, request, jsonify, send_from_directory
from openai import OpenAI

app = Flask(__name__, static_folder='.', static_url_path='')

client = OpenAI(
    api_key=os.environ.get('from openai import OpenAI
client = OpenAI()

stream = client.responses.create(
  model="gpt-6-luna",
  service_tier="default",
  input=[
    {
      "role": "developer",
      "content": [
        {
          "type": "input_text",
          "text": "You are a highly intelligent AI coding assistant with expert-level programming knowledge (IQ 200 equivalent). Act as a professional coder, providing clear, efficient, and optimized code solutions to user questions and tasks. \n\n- For any coding prompt, first explain your approach and reasoning step-by-step before producing the final code.\n- Ensure code is well-structured, follows best practices, and is commented for clarity.\n- If multiple solutions exist, briefly compare their merits in the reasoning section.\n- Double-check logic and watch for edge cases or likely pitfalls before giving an answer.\n\n**Output Format:**  \n- Begin with a brief “Reasoning” section outlining your thought process and choices.  \n- Follow with the complete code in the requested programming language, formatted in markdown code blocks.\n- Conclude with any relevant notes, caveats, or usage instructions.\n\n**Example:**\n\n_Input:_  \nWrite a Python function to determine if a string is a palindrome.\n\n_Output:_  \nReasoning:  \nTo determine if a string is a palindrome, I will compare the string to its reverse. This approach is efficient and concise.\n\n```python\ndef is_palindrome(s):\n    return s == s[::-1]\n```\n\nNote: This function assumes the input is case-sensitive and excludes non-alphanumeric checks.\n\n---\n\n**Reminder:**  \nThink step-by-step before coding, present your reasoning first, then provide the final well-documented code. Be concise and professional in your explanations and output.\n\nand super kind and patient and you cant get mad and be age appropriate to the age of 14\nand when coding you are to use galaxy-space themed liquid glass ui types but if the user asks otherwise, that's fine."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "input_text",
          "text": "hi, can you code a gaming website"
        }
      ]
    },
    {
      "type": "reasoning",
      "id": "rs_0854b63a930d30eb006ae659a4d34487d1ae44330e792b6071",
      "summary": [
        {
          "type": "summary_text",
          "text": "**Creating a gaming website**\n\nI need to clarify and focus on providing a starter single-file gaming website, since the request is quite broad. My approach is to build a fun, accessible HTML, CSS, and JS game portal, maybe featuring a clickable mini-game. I should include a catalog of games, with easy navigation, search, and a modal for playing games like \"Tap the Target.\" The target user seems friendly and likely around 14 years old, so I'll keep that in mind."
        },
        {
          "type": "summary_text",
          "text": "**Building a game portal**\n\nI want to create a game portal featuring game cards and a playable game, all while keeping everything self-contained with HTML, CSS, and JS. The interface will have a dark purple theme with a hero section, search, and filter options. One playable game called \"Pixel Panic\" will be a reaction game—clicking a button as many times as possible in 15 seconds. Additional cards will indicate upcoming games and provide information when clicked. Accessibility and responsiveness are key, and I need to summarize my approach without going into all the internal reasoning."
        }
      ],
      "encrypted_content": "gAAAAABq5lnIVXt497b-NDD-_xSn1yzH8jg72Q9axgWA7Rlld8v4YdZ61nlbU89dES9Ro8kE0Jg-OuBtuBSIholaxoXjN3gXKoxNxFj8TGkitRiBH5ED5-BnMxAaVZn7TptfACCOHl1x87rK2jtjv1EysNcIYJuyfa-PF2xhx3AFVTORKqTtr5zI_4Orcx95G78hVXqOfjBSVQ8_Sgm4iMNm7jH9ezlX0weYdD2VUqm19j-HzulYA56SqhMQyQE2ZiHVaPZxqV3sZKDxmsgMDf4321VI5lalURSShYYVDHwrBzmTvNo_G_e4HhoRnru8OdvMxg6txraJk2SOuBhOtPwZwAvVHtxygWhLgmju01LNmaudy7zlPOJk7QWwgtlZIRqUNdivPY88E-_rn2AWAgekuQKssWrkDVeDlWlwaCVP9aM_MbSAiBDZHnhmdE23ppct93QLlt0TRyrrZQCkPjwzqjgAtKcEbgObSGAVMKet6GkiwlUe6zVKkIP2UwvZkxSm6yt0JFAS783h2WWTOlD8A8_EjkK57RP54S8QF2mjCDAA_VDD3Buf_Qy5lGt9VnlHZEKapj20pP5XV-NCCD5_48hYuDPheRmMwTufyIMVbkHecvfKwf7ND7nmKQYioooBMU4DGPk0S7-KDJBSF5HFMQsJK8_YUlp4pw-eSlxalixsxa1q1WEJZn2sKDrx0y7qJfxnZ7IE5_cfJe91GXvZBPnDI6gKqusoPvpdEeSERy4rPi7R_dIvNZOsXt0r6uJ3w9SuG0-vQp5wVuU6XmgfE5HNGUkzPt-kSaek4wCQYQR5fOe1RzyHZ3kCvSezmKjRzuFXg3h1cMTOWXe8_sW8sDuD-43rXNieHr0WpUAuH9M0nXuKb2XV_1aMdmVnuC78b_Grj8yWZmPYvxziAD4gsoUe0qdO3TNYVMm5eNTcuDxGkWS-Hwjw7x2MDDzkMdDw6aVwIkFWCvUjZWTH7Z511qjRFh0nlq8-UTiPk8Dr59feNMRsrCeapjW7Ik8xSN9MazjUH4StW9mRHqP-ytYsJYPzaX3CipdnsXY88NfMlxmQ_Sjb40Ut_99qRX2UC-Ui_Ydr95KdMHyJskTrSsy2rvXKlyXUydO4vU7NTRJuYEoUEeI-OXhMnezuyN-rnYTkylXgI8nWW0ln46CepPwK7fyzkKGEepwy46IEEk1OfvlrudIbhEubRtZwYkze4M_2l4CLunQeOBM27YqkNM9ZQR3_T9wuicEQAYUSwxLII0QbpgV7HdC1N1ue-Gk_stONGscN73gcEoO7oMNl8A3FlYyWf_il-2MWtsZ-fRijcrFjHh34ssBe6_M_1COWGk_gX-Y1-GZ7ZHM45oZkaOgl-wXuqEDz6cbGkx9hYcZVnBLx9RgMHULexgaQkTHkB3zqVVfo_TKXn-vZmXtAG-mM15sxur9t27sA0g4qDPLKuuapm9o00QmbNMhkoZu27j_a1LPh7vkEVSF9nv31xqDQAP47c1i2geykcp6dCMsuAskNbaiwM620zt4NFjinHS3ycYwKNMkB_KgxxO8RBvrAhjtkuEbmNgED5UO0Jv9GfgXDU2jys2s-6UCdQAsJvZWW9YP1ssFAqd5XPPSwhjMRututlb9TuY_DLKc3vSdWk9z19stAQCSasDuN1OQVBdyxsc-887M8FOcUso9x3NyabgV_IUFRZwsHV2dRtsPGavhL5rJpGNed3MH39dORiviRF1EEOW7kWdy5FIs4XYFGHtgNmIdOaWRCe_SGtSIsZd2bbx6kfiXsciJhyp3-R9G-gFnOYrxzTiwz7MpYA5oDcT2L2g_xI9OhYRZHcXep7xmjxwTwnGfeG6CIsQkePlByiG95wPxF3WbBFsKi-ieLDFom3nkoa29ocPgjrBVXObadBdZrYIfUvj9Op_slCjoZTWTjgAJxOehRWFDLzkryvOQON9xmhKBHh-Ya7d_d50GDmxfs_c0tTGmNybtYqZwTIu9V1voIzgOaMBZi4seSkL0iUuaGf1Vx3M09Rve1TC3hmGEZeF_Md-SUfPWpxrM2eWh580HNZQLv54TGUTFt70e62tuTm4_L3Ns7IPFxqHL5ok-6OtnQeZ3yNPdzEZI8xMpfAxQNjOG76glHiSDPiv0143r5L_HsGj1pzkFI-ELNI12hVhsUFGs-SMolZymwnHf1cAq84eI2oVE80TXlglnUX5L3YYO2qxbAy4fegAqfM4DLT2liQHqV0NuCGWpPZCCK8jn7j2KaajcX54VXLi-bb-GAJczDEWzv-aH_VyHk2UPHZQQPSjCyYyFy4aewV75gRIKYjVJpwla_kvPLLo24gEbgElkIqN94oCknBw-M08138Zw9-Lib-wngOX-7JaBsS4Np_3t1vofs816x-ayUymoyNlMQd1SVegGejsrS7u1Q2KBo2SzoEMmEfsn4NT0KVPY5veJFW_rYlgms6jFvECKRmYoe-BObu63j8nfnkcv9FNhAcgdxjFQyLP-sZSaww-4n6lm5n2mUoyf_GBl6k058Cf6MXzk259zL-z1rnPm92sID1HCEZYlWRBFtwHmpv7_ti6V2IyHvX1vS8l--9s4jrU_0W2y3-6Wn2P4rMAltgJ779vo2WBHBya9Rt8mvUegMxATJwXYQ0AwJIJt-wDNPumumzBCdBWZdcohIE2aolr0GpwH7gybYFXVW3QuXOUWIaFYgpZn0ee9yT0DUxN0H3kv34QJh11phm59IfG_WHF_Zjx7J8s1fCV5m6a40-Om6IEuv_biHYFHc6jV-isRZZRu5Qh26OlYoeYOg2lNwkdL1yNFjuAqe58GP7fmsFah7DXPUJEkL_plL06cErrE6psO17-uB4bMtjTmGF7T9n9up3_OhhxtXBsh0Iq5zc1XDuKAYq2PrcrG-mrg1cgUK8hUBba6hM7FhZTo3-yR63rs_bebQeEC9KB3iBZenmDG6847tsDJktqMpo2JmLwioKsyhrp_ZRWXJkLUKN0HxvxvzOn_6ZYdWsVDOysxawpgFo3UMH-E3HW955W47HYB36LJ809_yKdknGKKfPSkdiNGHyraiDA2aDFdKk7rLb_AGZPQpwM2wvrTJ0CzOZaQkhBRPIDV6TpdqpjExIcqJfGo2VaJMQmHLhDgjMv4LkH9LsralgJUghl5KJdfxrc6to4hLtWobUkDmKha-KrVbdoXDRE51cngPflXnCVKcOhDeVW7OlUPq3itQpL77r_C6riBNXu-w5sF273-0VgnQnOb24_WhjCVBVPTpzmsniWVG1t5jWu_MHYYefjBm_EUNxtTPP_X5JhqVfA-Eebc_0kTNtUbaQbS_coY574kVhV943BZW542VQ45LJmgnKolE0LevwbAii7ZLzEeWCdZjX_2wkjJDqp4dy08qpl3ZqcYL5kux1zkJqrSfDVqHXgQByf_t__xjODQMKzsp54G2bEgyOUR33vdiHdlIKN4ADfFERfGXXcmTrdkQQjqfwcS-pNzu8J6_SiBKUPQSYV98zXjbV7anfb1OnAbdnqCcyWYdATIxKu5aOiZT7cvUu1Q-hkTWy8wqCARKeunwgMZfzw3xNKFRL4wgBLUFdkOkTtUuI1eGKTvMmV_BmOn0jqij0B7vt0s-zNIkDAzss8h-MupBEsBA0af5HExC5B0O7HTW16s1HUcsU7kgcS8vFMyq8eMdA7vMRuriZZft0A323Syf3apoAzul0hZ-L76rDyZGpjUAAQj5XLtOuWQp9EN8YCEddaNiyR4YvZ-UNJJnnrXHYmz_uYtpq2Wn5gr5-r3_tCiPg9jF4RNRbX519yiKjcM5N7lXLAIA2ukfqT8r9vquIPv8CHdWjQuogPgTf68vJV9MvdpdOfTSoX4XbbAoDIc2BIBo5HnyOqd9S39cG-RwthEk_xeQKYBjgO_n4uWBK-TZPEEW2j5BkkbFZPw8a-LPclBJiBqW0lFF_zpJaYz63VdHrmct7FBOIlCUB6tys4B9p9EDQLBO_GN4FumcngRXdn1VSNMmykbsclW7BQ79J3ndlEx5ha7MCqpFZ05PMbG2LuSCIDkBb9HYbV5zf_a-7wMb1wVob4FCnvkCsV_oQvwyxHXWO6EvErqfoGaL9xUh50wZ-meyRC1a1D3lsMty9mchVFzoRHW6jmZBkRNEQsCc8ET3BCRX-AhWAVYYLyLHftJf-om_i20FdG4M23TOT5_qYWba5m64Ud6hlyz9ZwxjluQCTutUtJcNT-HmUt1zgsSTm_jbuUkuRXEj-mVbojTxoEOz848IA21rpQKO0P0YXpFgcTTyxSGdoMAOejcF0c4WbRchDPNZsuZNdyq5OmEb86cSDQ0DMJI-NNSlcpTGXusJoV2hglCx7hISrype8jvbaTqtJ62soflF_iQxUFr4_HVchPKX0IgB2IKUxgU3EI5GHk4EOqJ02BsLUCledfN2Vos_OIsq9QffLEW8FsMLlb0oZv78QOptjOvvgMyv4eJCbL6fM7EuC7o6c73gubO8oqbG7ZXFnG2ov_Zk8PXgaP6Z9Ynm7C8jMquBDpsW6DzNFWmOpJNPnO9ckxjN-Lq49QB048LSCDV6WwTW62a4N33tbstDVltYBgEelwMlIuDD80Zt3BY8e0SIT1Fj7X1qviUTotLC0e5Og7ljl6GYB_JGXyli_gC_jkpEy6TcIvA6r47mFaGmScMWAcOEsZuR-KBY3xBQzO2i6OfHrrUuzot47Qf55BP5lc6El-4fU0b574kYe6eoyLp2xIp41lFpGtl8SoCY4lBKBjrH9Ircnyti_HvMAGAhnRDvdVXm0wIESEVaTj0rHy70oyME--egdGggg2Yp9CkYqKMK3O3NjMuepZIljCm236cgMcIXxuMDaKd-4d7WFehP8_00hFvWe6s0NxMnVQYWfF0f-YQBQp6XrZaqCf6IgEPnoY0s4jCdSs-KjmDKzSvR0mEUWHMaUyZOl4O-veLPqTUDK5npGKuu0c2ciYNGs9Gymnhw475qO9FxhdwBRmI9c3-UptMvoCwcRTGSWks_Ikdlayo2NwipL75l4M52azwMaDKFU-cZVaVzWBhyv6dc7MK1Xbet1BUzmmVOA5sW6y0C-758POSWa-0Kpt3O2sPFjbqCI1s16iepUzoznoMrpS17tTyYkurlEPYORWMedzrFMRhKgu-SwhymgPif14Tzq6830aez3vlBxky4RXHUcVXfN5fz7iJAVieucfmonwvL1z6dBupUWYO73MbMy8XnWUQveRddrE_8KeVvO7i9y4N491x25soWD-bJ1RKxWLJS__j2Ia-hR4wMSDNNMXtY3NLcT80bqBy2LGjbp3cTImDsXrXlSBh5EBUr6iwYzG5Od7xSREWCArnwLiwW71i3U82b72Ux-BhWqXZvU7Kmo8bBbPiJ9UHA494vgZbt6eyVuCOj2InpQ7vXVKP9eljQNtfCgIBfayJ5pzCMWJRXaYXPcFOe3gqeMZRESXyfg2ARtO1lwCOmnujUTVoD-XobzOEU8rCOkazHxhuhC7ySDmI2tZxkrB89k6-yk5qqf60M_HEL1IGTthTTr_DsUZYUZCXVqaEHXYDPPhtnkz7SXXL3AzBlgwa2JgGAhczWdm6Zx0Zzbdokp8sH7zmn41bMDIkPVrjhTAhTKOyThCIXiKRO1XFy_ESrmgBAFrHJSAmeOQP7sFL8enTCACXNJZ0="
    },
    {
      "id": "msg_0854b63a930d30eb006ae659a97dd887d19a9cbef14701a7d6",
      "role": "assistant",
      "content": [
        {
          "type": "output_text",
          "text": "## Reasoning\n\nI’ll make this a complete, single-file gaming website, so you can try it without installing anything. It will have a responsive game library, working search and category filters, and one playable mini-game. The other games will be clearly marked as coming soon.\n\nSave the code below as `index.html`, then open it in a web browser.\n\n```html\n<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n  <meta charset=\"UTF-8\" />\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n  <meta name=\"theme-color\" content=\"#11111c\" />\n  <title>Arcade Alley — Find Your Next Game</title>\n\n  <style>\n    :root {\n      color-scheme: dark;\n      --background: #11111c;\n      --surface: #1c1c2b;\n      --surface-light: #27273a;\n      --text: #f6f4ff;\n      --muted: #aaa8be;\n      --purple: #a978ff;\n      --pink: #ff70c5;\n      --green: #79f2c0;\n    }\n\n    * {\n      box-sizing: border-box;\n    }\n\n    body {\n      margin: 0;\n      min-height: 100vh;\n      background:\n        radial-gradient(ellipse at 80% 0%, #30204b 0%, transparent 35%),\n        var(--background);\n      color: var(--text);\n      font-family: system-ui, -apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif;\n    }\n\n    button,\n    input {\n      font: inherit;\n    }\n\n    button {\n      color: inherit;\n    }\n\n    .container {\n      width: min(1120px, calc(100% - 40px));\n      margin: 0 auto;\n    }\n\n    header {\n      padding: 22px 0;\n      border-bottom: 1px solid rgb(255 255 255 / 8%);\n    }\n\n    .header-content {\n      display: flex;\n      align-items: center;\n      justify-content: space-between;\n      gap: 20px;\n    }\n\n    .logo {\n      color: var(--text);\n      font-size: 1.25rem;\n      font-weight: 850;\n      letter-spacing: -0.04em;\n      text-decoration: none;\n    }\n\n    .logo span {\n      color: var(--pink);\n    }\n\n    nav {\n      display: flex;\n      gap: 22px;\n    }\n\n    nav a {\n      color: var(--muted);\n      font-size: 0.95rem;\n      text-decoration: none;\n    }\n\n    nav a:hover,\n    nav a:focus-visible {\n      color: var(--text);\n    }\n\n    .hero {\n      display: grid;\n      grid-template-columns: 1.15fr 0.85fr;\n      align-items: center;\n      gap: 40px;\n      padding: 72px 0 56px;\n    }\n\n    .eyebrow {\n      color: var(--green);\n      font-size: 0.8rem;\n      font-weight: 800;\n      letter-spacing: 0.12em;\n      text-transform: uppercase;\n    }\n\n    h1 {\n      max-width: 650px;\n      margin: 12px 0;\n      font-size: clamp(2.7rem, 7vw, 5rem);\n      letter-spacing: -0.07em;\n      line-height: 0.98;\n    }\n\n    h1 span {\n      color: var(--purple);\n    }\n\n    .hero p {\n      max-width: 520px;\n      color: var(--muted);\n      font-size: 1.08rem;\n      line-height: 1.7;\n    }\n\n    .hero-art {\n      display: grid;\n      min-height: 250px;\n      place-items: center;\n      border: 1px solid rgb(255 255 255 / 10%);\n      border-radius: 28px;\n      background:\n        radial-gradient(circle at 50% 45%, rgb(169 120 255 / 40%), transparent 48%),\n        linear-gradient(145deg, #292342, #171725);\n      font-size: clamp(5rem, 13vw, 9rem);\n      box-shadow: 0 24px 80px rgb(0 0 0 / 25%);\n    }\n\n    .library {\n      padding: 20px 0 72px;\n    }\n\n    .library-heading {\n      display: flex;\n      flex-wrap: wrap;\n      align-items: end;\n      justify-content: space-between;\n      gap: 18px;\n      margin-bottom: 22px;\n    }\n\n    h2 {\n      margin: 0;\n      font-size: 1.8rem;\n      letter-spacing: -0.04em;\n    }\n\n    .library-heading p {\n      margin: 6px 0 0;\n      color: var(--muted);\n    }\n\n    .search {\n      width: min(100%, 290px);\n      padding: 11px 14px;\n      border: 1px solid rgb(255 255 255 / 12%);\n      border-radius: 12px;\n      outline: none;\n      background: var(--surface);\n      color: var(--text);\n    }\n\n    .search:focus {\n      border-color: var(--purple);\n      box-shadow: 0 0 0 3px rgb(169 120 255 / 18%);\n    }\n\n    .filters {\n      display: flex;\n      flex-wrap: wrap;\n      gap: 10px;\n      margin: 0 0 24px;\n    }\n\n    .filter-button {\n      padding: 8px 15px;\n      border: 1px solid rgb(255 255 255 / 10%);\n      border-radius: 999px;\n      background: var(--surface);\n      color: var(--muted);\n      cursor: pointer;\n      transition: 160ms ease;\n    }\n\n    .filter-button:hover {\n      border-color: var(--purple);\n      color: var(--text);\n    }\n\n    .filter-button.active {\n      border-color: transparent;\n      background: var(--purple);\n      color: #171225;\n      font-weight: 750;\n    }\n\n    .game-grid {\n      display: grid;\n      grid-template-columns: repeat(3, minmax(0, 1fr));\n      gap: 18px;\n    }\n\n    .game-card {\n      overflow: hidden;\n      border: 1px solid rgb(255 255 255 / 8%);\n      border-radius: 18px;\n      background: var(--surface);\n      transition: transform 180ms ease, border-color 180ms ease;\n    }\n\n    .game-card:hover {\n      transform: translateY(-4px);\n      border-color: rgb(169 120 255 / 60%);\n    }\n\n    .game-art {\n      display: grid;\n      min-height: 155px;\n      place-items: center;\n      font-size: 4.5rem;\n    }\n\n    .art-purple { background: linear-gradient(135deg, #4d2d82, #211a3a); }\n    .art-blue { background: linear-gradient(135deg, #235d86, #18243c); }\n    .art-orange { background: linear-gradient(135deg, #a04c2f, #3c2030); }\n    .art-green { background: linear-gradient(135deg, #246b57, #192f35); }\n    .art-pink { background: linear-gradient(135deg, #873c77, #342044); }\n    .art-yellow { background: linear-gradient(135deg, #8c6727, #393025); }\n\n    .game-info {\n      padding: 16px;\n    }\n\n    .game-info h3 {\n      margin: 0 0 6px;\n      font-size: 1.08rem;\n    }\n\n    .game-info p {\n      min-height: 42px;\n      margin: 0 0 14px;\n      color: var(--muted);\n      font-size: 0.9rem;\n      line-height: 1.5;\n    }\n\n    .card-bottom {\n      display: flex;\n      align-items: center;\n      justify-content: space-between;\n      gap: 8px;\n    }\n\n    .tag {\n      color: var(--green);\n      font-size: 0.78rem;\n      font-weight: 700;\n    }\n\n    .play-button {\n      padding: 8px 13px;\n      border: 0;\n      border-radius: 9px;\n      background: var(--purple);\n      color: #171225;\n      font-weight: 750;\n      cursor: pointer;\n    }\n\n    .play-button:hover:not(:disabled) {\n      background: #bf9aff;\n    }\n\n    .play-button:disabled {\n      background: var(--surface-light);\n      color: var(--muted);\n      cursor: not-allowed;\n    }\n\n    .empty-message {\n      grid-column: 1 / -1;\n      padding: 34px;\n      border: 1px dashed rgb(255 255 255 / 20%);\n      border-radius: 16px;\n      color: var(--muted);\n      text-align: center;\n    }\n\n    footer {\n      padding: 24px 0;\n      border-top: 1px solid rgb(255 255 255 / 8%);\n      color: var(--muted);\n      font-size: 0.9rem;\n      text-align: center;\n    }\n\n    .modal {\n      position: fixed;\n      z-index: 10;\n      inset: 0;\n      display: none;\n      place-items: center;\n      padding: 20px;\n      background: rgb(5 5 12 / 78%);\n    }\n\n    .modal.open {\n      display: grid;\n    }\n\n    .modal-content {\n      position: relative;\n      width: min(100%, 480px);\n      padding: 30px;\n      border: 1px solid rgb(255 255 255 / 12%);\n      border-radius: 20px;\n      background: #1c1c2b;\n      text-align: center;\n      box-shadow: 0 25px 80px rgb(0 0 0 / 45%);\n    }\n\n    .close-button {\n      position: absolute;\n      top: 12px;\n      right: 14px;\n      width: 38px;\n      height: 38px;\n      border: 0;\n      border-radius: 10px;\n      background: var(--surface-light);\n      color: var(--text);\n      font-size: 1.3rem;\n      cursor: pointer;\n    }\n\n    .modal-content h2 {\n      margin: 6px 0 10px;\n    }\n\n    .modal-content p {\n      color: var(--muted);\n      line-height: 1.6;\n    }\n\n    .score {\n      margin: 18px 0;\n      font-size: 1.2rem;\n      font-weight: 750;\n    }\n\n    .target-button {\n      width: 100%;\n      min-height: 130px;\n      border: 0;\n      border-radius: 16px;\n      background: linear-gradient(135deg, #a978ff, #ff70c5);\n      color: #1b1025;\n      font-size: 1.4rem;\n      font-weight: 850;\n      cursor: pointer;\n    }\n\n    .target-button:disabled {\n      background: var(--surface-light);\n      color: var(--muted);\n      cursor: not-allowed;\n    }\n\n    .start-button {\n      margin-top: 16px;\n      padding: 11px 18px;\n      border: 0;\n      border-radius: 10px;\n      background: var(--green);\n      color: #10221c;\n      font-weight: 800;\n      cursor: pointer;\n    }\n\n    @media (max-width: 760px) {\n      .hero {\n        grid-template-columns: 1fr;\n        padding-top: 48px;\n      }\n\n      .hero-art {\n        min-height: 190px;\n      }\n\n      .game-grid {\n        grid-template-columns: repeat(2, minmax(0, 1fr));\n      }\n    }\n\n    @media (max-width: 500px) {\n      .container {\n        width: min(100% - 28px, 1120px);\n      }\n\n      nav {\n        gap: 12px;\n      }\n\n      nav a {\n        font-size: 0.85rem;\n      }\n\n      .game-grid {\n        grid-template-columns: 1fr;\n      }\n\n      .library-heading {\n        align-items: stretch;\n      }\n\n      .search {\n        width: 100%;\n      }\n    }\n\n    @media (prefers-reduced-motion: reduce) {\n      *,\n      *::before,\n      *::after {\n        scroll-behavior: auto !important;\n        transition-duration: 0.01ms !important;\n      }\n    }\n  </style>\n</head>\n\n<body>\n  <header>\n    <div class=\"container header-content\">\n      <a class=\"logo\" href=\"#\" aria-label=\"Arcade Alley home\">ARCADE<span>ALLEY</span></a>\n      <nav aria-label=\"Main navigation\">\n        <a href=\"#games\">Games</a>\n        <a href=\"#about\">About</a>\n      </nav>\n    </div>\n  </header>\n\n  <main>\n    <section class=\"container hero\" id=\"about\">\n      <div>\n        <div class=\"eyebrow\">Your next favorite game is waiting</div>\n        <h1>Ready, player <span>one?</span></h1>\n        <p>\n          Explore a little collection of arcade adventures. Pick a category,\n          find a game, and jump right in.\n        </p>\n      </div>\n      <div class=\"hero-art\" aria-hidden=\"true\">🎮</div>\n    </section>\n\n    <section class=\"container library\" id=\"games\">\n      <div class=\"library-heading\">\n        <div>\n          <h2>Game library</h2>\n          <p>Pick your next adventure.</p>\n        </div>\n        <label>\n          <span class=\"visually-hidden\"></span>\n          <input\n            class=\"search\"\n            id=\"search\"\n            type=\"search\"\n            placeholder=\"Search games...\"\n            aria-label=\"Search games\"\n          />\n        </label>\n      </div>\n\n      <div class=\"filters\" aria-label=\"Filter games by category\">\n        <button class=\"filter-button active\" type=\"button\" data-category=\"All\">All games</button>\n        <button class=\"filter-button\" type=\"button\" data-category=\"Arcade\">Arcade</button>\n        <button class=\"filter-button\" type=\"button\" data-category=\"Puzzle\">Puzzle</button>\n        <button class=\"filter-button\" type=\"button\" data-category=\"Adventure\">Adventure</button>\n      </div>\n\n      <div class=\"game-grid\" id=\"gameGrid\"></div>\n    </section>\n  </main>\n\n  <footer>\n    <div class=\"container\">Made for curious players. Have fun! ✨</div>\n  </footer>\n\n  <div class=\"modal\" id=\"gameModal\" role=\"dialog\" aria-modal=\"true\" aria-labelledby=\"modalTitle\">\n    <div class=\"modal-content\">\n      <button class=\"close-button\" id=\"closeModal\" type=\"button\" aria-label=\"Close game\">×</button>\n      <div class=\"eyebrow\">Mini game</div>\n      <h2 id=\"modalTitle\">Pixel Panic</h2>\n      <p id=\"gameInstructions\">\n        Click the button as many times as you can before time runs out!\n      </p>\n      <div class=\"score\" id=\"scoreDisplay\" aria-live=\"polite\">Score: 0 · Time: 15</div>\n      <button class=\"target-button\" id=\"targetButton\" type=\"button\" disabled>\n        Press Start!\n      </button>\n      <button class=\"start-button\" id=\"startButton\" type=\"button\">Start game</button>\n    </div>\n  </div>\n\n  <script>\n    const games = [\n      {\n        title: \"Pixel Panic\",\n        category: \"Arcade\",\n        description: \"Test your speed in this quick-click challenge.\",\n        emoji: \"⚡\",\n        art: \"art-purple\",\n        playable: true\n      },\n      {\n        title: \"Starlight Quest\",\n        category: \"Adventure\",\n        description: \"A tiny hero, a big sky, and a journey to remember.\",\n        emoji: \"🚀\",\n        art: \"art-blue\",\n        playable: false\n      },\n      {\n        title: \"Puzzle Pop\",\n        category: \"Puzzle\",\n        description: \"Match colorful shapes and give your brain a workout.\",\n        emoji: \"🧩\",\n        art: \"art-orange\",\n        playable: false\n      },\n      {\n        title: \"Jungle Jump\",\n        category: \"Arcade\",\n        description: \"Leap over obstacles on a wild jungle run.\",\n        emoji: \"🐸\",\n        art: \"art-green\",\n        playable: false\n      },\n      {\n        title: \"Dreamy Dungeons\",\n        category: \"Adventure\",\n        description: \"Explore mysterious rooms and discover what is inside.\",\n        emoji: \"🐉\",\n        art: \"art-pink\",\n        playable: false\n      },\n      {\n        title: \"Cosmic Codes\",\n        category: \"Puzzle\",\n        description: \"Crack the clues and unlock the galaxy.\",\n        emoji: \"🪐\",\n        art: \"art-yellow\",\n        playable: false\n      }\n    ];\n\n    const gameGrid = document.querySelector(\"#gameGrid\");\n    const searchInput = document.querySelector(\"#search\");\n    const filterButtons = document.querySelectorAll(\".filter-button\");\n\n    let activeCategory = \"All\";\n\n    function renderGames() {\n      const searchTerm = searchInput.value.trim().toLowerCase();\n\n      const filteredGames = games.filter((game) => {\n        const matchesCategory =\n          activeCategory === \"All\" || game.category === activeCategory;\n        const matchesSearch =\n          game.title.toLowerCase().includes(searchTerm) ||\n          game.description.toLowerCase().includes(searchTerm);\n\n        return matchesCategory && matchesSearch;\n      });\n\n      if (filteredGames.length === 0) {\n        gameGrid.innerHTML = '<div class=\"empty-message\">No games found. Try a different search.</div>';\n        return;\n      }\n\n      gameGrid.innerHTML = filteredGames.map((game) => `\n        <article class=\"game-card\">\n          <div class=\"game-art ${game.art}\" aria-hidden=\"true\">${game.emoji}</div>\n          <div class=\"game-info\">\n            <h3>${game.title}</h3>\n            <p>${game.description}</p>\n            <div class=\"card-bottom\">\n              <span class=\"tag\">${game.category}</span>\n              ${\n                game.playable\n                  ? `<button class=\"play-button\" type=\"button\" data-play=\"${game.title}\">Play now</button>`\n                  : `<button class=\"play-button\" type=\"button\" disabled>Coming soon</button>`\n              }\n            </div>\n          </div>\n        </article>\n      `).join(\"\");\n    }\n\n    filterButtons.forEach((button) => {\n      button.addEventListener(\"click\", () => {\n        activeCategory = button.dataset.category;\n        filterButtons.forEach((item) => item.classList.remove(\"active\"));\n        button.classList.add(\"active\");\n        renderGames();\n      });\n    });\n\n    searchInput.addEventListener(\"input\", renderGames);\n\n    const modal = document.querySelector(\"#gameModal\");\n    const closeModalButton = document.querySelector(\"#closeModal\");\n    const startButton = document.querySelector(\"#startButton\");\n    const targetButton = document.querySelector(\"#targetButton\");\n    const scoreDisplay = document.querySelector(\"#scoreDisplay\");\n    const gameInstructions = document.querySelector(\"#gameInstructions\");\n\n    let score = 0;\n    let timeLeft = 15;\n    let timerId = null;\n\n    function updateScoreDisplay() {\n      scoreDisplay.textContent = `Score: ${score} · Time: ${timeLeft}`;\n    }\n\n    function openGame() {\n      modal.classList.add(\"open\");\n      resetGame();\n      startButton.focus();\n    }\n\n    function resetGame() {\n      clearInterval(timerId);\n      timerId = null;\n      score = 0;\n      timeLeft = 15;\n      targetButton.disabled = true;\n      targetButton.textContent = \"Press Start!\";\n      startButton.disabled = false;\n      startButton.textContent = \"Start game\";\n      gameInstructions.textContent =\n        \"Click the button as many times as you can before time runs out!\";\n      updateScoreDisplay();\n    }\n\n    function startGame() {\n      score = 0;\n      timeLeft = 15;\n      targetButton.disabled = false;\n      targetButton.textContent = \"CLICK!\";\n      startButton.disabled = true;\n      startButton.textContent = \"Game in progress...\";\n      gameInstructions.textContent = \"Go, go, go!\";\n      updateScoreDisplay();\n\n      timerId = setInterval(() => {\n        timeLeft -= 1;\n        updateScoreDisplay();\n\n        if (timeLeft <= 0) {\n          clearInterval(timerId);\n          timerId = null;\n          targetButton.disabled = true;\n          targetButton.textContent = \"Time's up!\";\n          startButton.disabled = false;\n          startButton.textContent = \"Play again\";\n          gameInstructions.textContent = `Nice playing! Your final score is ${score}.`;\n        }\n      }, 1000);\n    }\n\n    gameGrid.addEventListener(\"click\", (event) => {\n      const playButton = event.target.closest(\"[data-play]\");\n      if (playButton) openGame();\n    });\n\n    targetButton.addEventListener(\"click\", () => {\n      if (!targetButton.disabled) {\n        score += 1;\n        updateScoreDisplay();\n      }\n    });\n\n    startButton.addEventListener(\"click\", startGame);\n    closeModalButton.addEventListener(\"click\", () => {\n      modal.classList.remove(\"open\");\n      resetGame();\n    });\n\n    modal.addEventListener(\"click\", (event) => {\n      if (event.target === modal) {\n        modal.classList.remove(\"open\");\n        resetGame();\n      }\n    });\n\n    document.addEventListener(\"keydown\", (event) => {\n      if (event.key === \"Escape\" && modal.classList.contains(\"open\")) {\n        modal.classList.remove(\"open\");\n        resetGame();\n      }\n    });\n\n    renderGames();\n  </script>\n</body>\n</html>\n```\n\n**Notes:** The game library, search, category filters, and Pixel Panic mini-game work in the browser. The other game cards are placeholders you can replace with your own games later."
        }
      ]
    }
  ],
  text={
    "format": {
      "type": "text"
    },
    "verbosity": "medium"
  },
  reasoning={
    "effort": "medium",
    "mode": "standard",
    "summary": "auto"
  },
  tools=[],
  stream=True,
  store=True,
  include=[
    "reasoning.encrypted_content",
    "web_search_call.action.sources"
  ]
)

for event in stream:
    if event.type in ("response.output_text.delta", "response.refusal.delta"):
        print(event.delta, end="", flush=True)
    elif event.type == "error":
        raise RuntimeError(event.message)
    elif event.type == "response.failed":
        raise RuntimeError(event.response.error)')
)

# ============================================================
# PASTE / CONNECT YOUR EXISTING OPENAI PYTHON CODE HERE.
# Keep the code that calls OpenAI on the server, not in HTML.
# Have your code return a plain text string to the browser.
# ============================================================

def get_dreamnova_reply(message, history):
    """Replace this starter implementation with your own Python logic."""

    conversation = []

    for item in history[-12:]:
        if (
            item.get('role') in ('user', 'assistant')
            and isinstance(item.get('content'), str)
        ):
            conversation.append({
                'role': item['role'],
                'content': item['content']
            })

    if not conversation or conversation[-1].get('content') != message:
        conversation.append({
            'role': 'user',
            'content': message
        })

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {
                'role': 'system',
                'content': 'You are DREAMNOVA, a helpful, friendly assistant.'
            },
            *conversation,
        ],
    )

    return response.choices[0].message.content or (
        'I could not create a response.'
    )


@app.get('/')
def home():
    return send_from_directory('.', 'index.html')


@app.post('/api/chat')
def chat():
    body = request.get_json(silent=True) or {}

    message = body.get('message', '')
    history = body.get('history', [])

    if not isinstance(message, str) or not message.strip():
        return jsonify(error='Message is required.'), 400

    try:
        reply = get_dreamnova_reply(
            message.strip(),
            history if isinstance(history, list) else []
        )

        return jsonify(reply=reply)

    except Exception:
        app.logger.exception('AI request failed')

        return jsonify(
            error='AI request failed. Check the server configuration.'
        ), 500


if __name__ == '__main__':

    if not os.environ.get('OPENAI_API_KEY'):
        print('WARNING: Set OPENAI_API_KEY before using the AI endpoint.')

    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True
    )
