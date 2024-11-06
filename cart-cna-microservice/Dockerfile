
FROM openjdk:17-alpine

RUN apk add --no-cache bash curl && \
apk add --no-cache bash zip && \
curl -s "https://get.sdkman.io" | bash && \
bash -c "source $HOME/.sdkman/bin/sdkman-init.sh && sdk install gradle 7.5"

WORKDIR /app
COPY . .
RUN export $(cat .env | xargs)
RUN $HOME/.sdkman/candidates/gradle/current/bin/gradle build
# ARG JAR_FILE=/app/build/libs/cart-1.0.0.jar
RUN cp /app/build/libs/cart-1.0.0.jar /app/app.jar

RUN addgroup -S spring && adduser -S spring -G spring
RUN chown -R spring:spring /app
USER spring:spring
ENTRYPOINT ["java","-jar","/app/app.jar"]