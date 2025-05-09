#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from colorama import init, Fore
from modules import name_search, phone_search, ip_analysis, image_analysis, email_osint

# Initialize colorama
init()

ANON_ATLAS_ART = f"""
{Fore.MAGENTA}
   █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗ █████╗ ████████╗██╗      █████╗ ███████╗
  ██╔══██╗████╗  ██║██╔═══██╗████╗  ██║██╔══██╗╚══██╔══╝██║     ██╔══██╗██╔════╝
  ███████║██╔██╗ ██║██║   ██║██╔██╗ ██║███████║   ██║   ██║     ███████║███████╗
  ██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║██╔══██║   ██║   ██║     ██╔══██║╚════██║
  ██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║██║  ██║   ██║   ███████╗██║  ██║███████║
  ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝
{Fore.CYAN}
  ┌──────────────────────────────────────────────────────────────────────────────┐
  │   ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ █████╗ ██╗   │
  │  ██╔═══██╗██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║   │
  │  ██║   ██║█████╗  ██╔██╗ ██║███████╗██████╔╝███████║   ██║   ███████║██║   │
  │  ██║   ██║██╔══╝  ██║╚██╗██║╚════██║██╔═══╝ ██╔══██║   ██║   ██╔══██║██║   │
  │  ╚██████╔╝███████╗██║ ╚████║███████║██║     ██║  ██║   ██║   ██║  ██║██║   │
  │   ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝   │
  └──────────────────────────────────────────────────────────────────────────────┘
{Fore.RESET}
"""

def show_menu():
    print(ANON_ATLAS_ART)
    print(f"{Fore.YELLOW}╔════════════════════════════════════════════════════════════════════════╗")
    print(f"║{Fore.CYAN}                  أداة OSINT متكاملة - فريق أنون أطلس{Fore.YELLOW}                 ║")
    print(f"╠════════════════════════════════════════════════════════════════════════╣")
    print(f"║{Fore.GREEN} 1. جمع بيانات وحسابات عن طريق الاسم{Fore.YELLOW}                          ║")
    print(f"║{Fore.GREEN} 2. جمع بيانات وحسابات عن طريق الرقم{Fore.YELLOW}                          ║")
    print(f"║{Fore.GREEN} 3. فحص وجمع أدلة على IP{Fore.YELLOW}                                     ║")
    print(f"║{Fore.GREEN} 4. تحليل الصور ومصدرها{Fore.YELLOW}                                      ║")
    print(f"║{Fore.GREEN} 5. معرفة معلومات عن إيميل ومصادره وحساباته{Fore.YELLOW}                   ║")
    print(f"║{Fore.RED} 0. الخروج{Fore.YELLOW}                                                   ║")
    print(f"╚════════════════════════════════════════════════════════════════════════╝{Fore.RESET}")

def main():
    while True:
        show_menu()
        choice = input(f"{Fore.CYAN}↳ اختر رقم الخيار (0-5): {Fore.RESET}").strip()

        if choice == "1":
            name = input(f"{Fore.BLUE}↳ أدخل الاسم المستهدف: {Fore.RESET}").strip()
            print(f"\n{Fore.YELLOW}جارٍ البحث...{Fore.RESET}")
            results = name_search.search_by_name(name)
            print(f"\n{Fore.GREEN}النتائج:{Fore.RESET}")
            for platform, url in results.items():
                print(f"{Fore.CYAN}{platform}: {Fore.WHITE}{url}")

        elif choice == "2":
            phone = input(f"{Fore.BLUE}↳ أدخل الرقم المستهدف (مثال: +123456789): {Fore.RESET}").strip()
            print(f"\n{Fore.YELLOW}جارٍ البحث...{Fore.RESET}")
            results = phone_search.search_by_phone(phone)
            print(f"\n{Fore.GREEN}النتائج:{Fore.RESET}")
            print(results)

        elif choice == "3":
            ip = input(f"{Fore.BLUE}↳ أدخل عنوان IP المستهدف (مثال: 8.8.8.8): {Fore.RESET}").strip()
            print(f"\n{Fore.YELLOW}جارٍ الفحص...{Fore.RESET}")
            results = ip_analysis.analyze_ip(ip)
            print(f"\n{Fore.GREEN}النتائج:{Fore.RESET}")
            print(results)

        elif choice == "4":
            image_path = input(f"{Fore.BLUE}↳ أدخل مسار الصورة (مثال: photo.jpg): {Fore.RESET}").strip()
            print(f"\n{Fore.YELLOW}جارٍ التحليل...{Fore.RESET}")
            results = image_analysis.analyze_image(image_path)
            print(f"\n{Fore.GREEN}النتائج:{Fore.RESET}")
            print(results)

        elif choice == "5":
            email = input(f"{Fore.BLUE}↳ أدخل البريد الإلكتروني المستهدف (مثال: test@example.com): {Fore.RESET}").strip()
            print(f"\n{Fore.YELLOW}جارٍ البحث...{Fore.RESET}")
            results = email_osint.analyze_email(email)
            print(f"\n{Fore.GREEN}النتائج:{Fore.RESET}")
            print(results)

        elif choice == "0":
            print(f"\n{Fore.MAGENTA}تم الخروج من الأداة. مع السلامة 👋{Fore.RESET}")
            break

        else:
            print(f"\n{Fore.RED}⚠️ خيار غير صحيح! يرجى اختيار رقم بين 0 و5.{Fore.RESET}")

        input(f"\n{Fore.YELLOW}اضغط على Enter للعودة إلى القائمة...{Fore.RESET}")

if __name__ == "__main__":
    main()