'''

$ curl -X POST -d "username=hari&password=harihari" http://localhost:8000/api-token-auth/

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImhhcmkiLCJ1c2VyX2lkIjoxLCJlbWFpbCI6ImhhcmlwcmFzYXRoaGFyaTkyOTJAZ21haWwuY29tIiwiZXhwIjoxNDkwNTIwMDIxfQ.4GIOBFUCrXqXOf6Buvv4J-vvti1dhjjyreeMLl0_UPM




$ curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImhhcmkiLCJ1c2VyX2lkIjoxLCJlbWFpbCI6ImhhcmlwcmFzYXRoaGFyaTkyOTJAZ21haWwuY29tIiwiZXhwIjoxNDkwNTIwMDIxfQ.4GIOBFUCrXqXOf6Buvv4J-vvti1dhjjyreeMLl0_UPM
" http://localhost:8000/protected-url/


curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImhhcmkiLCJ1c2VyX2lkIjoxLCJlbWFpbCI6ImhhcmlwcmFzYXRoaGFyaTkyOTJAZ21haWwuY29tIiwiZXhwIjoxNDkwNTIwMDIxfQ.4GIOBFUCrXqXOf6Buvv4J-vvti1dhjjyreeMLl0_UPM
" http://localhost:8000/users/profile/1/

curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImhhcmkiLCJ1c2VyX2lkIjoxLCJlbWFpbCI6ImhhcmlwcmFzYXRoaGFyaTkyOTJAZ21haWwuY29tIiwiZXhwIjoxNDkwNTIwMDIxfQ.4GIOBFUCrXqXOf6Buvv4J-vvti1dhjjyreeMLl0_UPM
" http://localhost:8000/users/profile/2/


eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJlbWFpbCI6ImhhcmlwcmFzYXRoaGFyaTkyOTJAZ21haWwuY29tIiwidXNlcm5hbWUiOiJoYXJpIiwiZXhwIjoxNDkwNTIwNTYzfQ.gKiPQuJOisS8Y7HJrO8Jbmrb7r-uy1dzxKk6RGs3F7g

curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJlbWFpbCI6ImhhcmlwcmFzYXRoaGFyaTkyOTJAZ21haWwuY29tIiwidXNlcm5hbWUiOiJoYXJpIiwiZXhwIjoxNDkwNTIwNTYzfQ.gKiPQuJOisS8Y7HJrO8Jbmrb7r-uy1dzxKk6RGs3F7g
" http://localhost:8000/protected-url/



curl -X POST -H "Content-Type: application/json" -d '{"username":"123456789876","password":"harihari"}' http://localhost:8000/api-token-auth/

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo2LCJlbWFpbCI6IiIsInVzZXJuYW1lIjoiMTIzNDU2Nzg5ODc2IiwiZXhwIjoxNDkwNTIwNzc4fQ.Ribq1acbCaUu000x3ON3K03bGAorXr_12eIkd3U854s



curl -X POST -H "Authorization: JWT <token>" -H "Content-Type: application/json" -d '{"content":"my new reply to another try"}' 'http://127.0.0.1:8000/api/comments/create/?slug=new-title&type=post&parent_id=13'



curl -X POST -H "Authorization: JWT <token>" -H "Content-Type: application/json" -d '{"content":"my new reply to another try"}' 'http://127.0.0.1:8000/api/comments/create/?slug=new-title&type=post&parent_id=13'


eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImhhcmlwcmFzYXRoaGFyaTkyOTJAZ21haWwuY29tIiwiZXhwIjoxNDkwNjA5MTYzLCJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImhhcmkifQ.hSTsi0QRonyLKBZAgwaLiIgYXCLgO6LDRpKNlYzTgmw


curl -X POST -d "username=harihari&password=harihari" http://gctportal.com:7575/api-token-auth/

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImhhcmloYXJpIiwiZXhwIjoxNDkwODUxNzkzLCJlbWFpbCI6IiIsInVzZXJfaWQiOjJ9.c7rPsNYdXakx8RZUTgftjr9pwFoQHPDJtL3UqUrxDPE"

curl http://gctportal.com:7575/app/schemes/

'''

